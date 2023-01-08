# utils.py 
import importlib

def import_module(module_name: str) -> object:
    return importlib.import_module(module_name)
