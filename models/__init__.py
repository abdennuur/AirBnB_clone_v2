#!/usr/bin/python3
"""To instantiate storage objct.

-> If environmental var 'HBNB_TYPE_STORAGE' set to 'db',
   instantiate database storage engine (DBStorage).
-> Otherwise, instantiates file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
