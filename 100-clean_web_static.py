#!/usr/bin/python3
"""the web server distribution"""
from fabric.api import *
from fabric.state import commands, connections
import os.path

env.user = 'ubuntu'
env.hosts = ["54.227.197.165", "35.174.200.96"]
env.key_filename = "~/id_rsa"


def do_clean(number=0):
    """deletes out-of-date archives"""
    local('ls -t ~/AirBnB_Clone_V2/versions/').split()
    with cd("/data/web_static/releases"):
        target_R = sudo("ls -t .").split()
    paths = "/data/web_static/releases"
    nbr = int(nbr)
    if nbr == 0:
        num = 1
    else:
        num = nbr
    if len(target_R) > 0:
        if len(target) == nbr or len(target) == 0:
            pass
        else:
            clr = target[num:]
            for ix in range(len(clr)):
                local('rm -f ~/AirBnB_Clone_V2/versions/{}'.format(target[-1]))
        rem = target_R[num:]
        for ji in range(len(rem)):
            sudo('rm -rf {}/{}'.format(paths, rem[-1].strip(".tgz")))
    else:
        pass
