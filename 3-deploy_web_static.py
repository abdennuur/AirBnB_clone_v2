#!/usr/bin/python3
# Fabfile t create and distribute archive to web server.
import os.path
from datetime import datetime
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ["54.227.197.165", "35.174.200.96"]


def do_pack():
    """Creates tar g zipped archive of dir web_static."""
    dtm = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dtm.year,
                                                         dtm.month,
                                                         dtm.day,
                                                         dtm.hour,
                                                         dtm.minute,
                                                         dtm.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes archive to web server.
    Args:
        archive_path (str): path of the archive to distribute.
    Returns:
        If file doesn't exist at archive_path or error occurs - False.
        Otherwise - True.
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


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
