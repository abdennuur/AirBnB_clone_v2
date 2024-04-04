#!/usr/bin/python3
# Fabfile 2 delete out-of-date archives
import os
from fabric.api import *

env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_clean(number=0):
    """Delete out-of-date archive
    Args:
        number (int): number of archives to keep
    If number 0 or 1, keep only most recent archive. If
    nber is 2, keep the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for ix in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archive]

    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [a for a in archive if "web_static_" in a]
        [archive.pop() for ix in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archive]
