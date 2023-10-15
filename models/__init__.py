#!/usr/bin/pythoon3
"""
Initialization file for python3 package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
