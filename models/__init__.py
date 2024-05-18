#!/usr/bin/python3
""" Importing models file_storage to use -> storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
