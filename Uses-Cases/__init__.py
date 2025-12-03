import sys
import os

uses_cases_dir = os.path.dirname(__file__)
for name in os.listdir(uses_cases_dir):
    subdir = os.path.join(uses_cases_dir, name)
    if os.path.isdir(subdir) and not name.startswith(('.', '_')):
        if subdir not in sys.path:
            sys.path.insert(0, subdir)
