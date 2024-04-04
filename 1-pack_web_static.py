#!/usr/bin/python3
# Fabfile to generate a .tgz archive frm contents of the web_static
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
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
