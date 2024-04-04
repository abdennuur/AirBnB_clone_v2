#!/usr/bin/python3
# Fabfile to distribute archive to web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_deploy(archive_path):
    """Distribut archive to web server
    Args:
        archive_path (str): path of archive to distribute.
    Returns:
        If file doesn't exist at archive_path or error occurs - False.
        Othrwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    nme = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(nme)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(nme)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, nme)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(nme, nme)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(nme)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(nme)).failed is True:
        return False
    return True
