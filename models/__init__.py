#!/usr/bin/env python3
''' These run when importing models '''
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
