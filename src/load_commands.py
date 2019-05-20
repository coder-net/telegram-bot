import importlib
import re
from os import listdir


directory = 'commands'
files = listdir(directory)
modules = filter(lambda file: re.match(r'\w+\.py', file), files)
for module in modules:
    importlib.import_module('{}.{}'.format(directory, module[:-3]))
