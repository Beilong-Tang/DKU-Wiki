#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import json

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki_backend.settings')
    settings = json.load(open((os.path.join('.config','settings.json')),'r'))
    for key,value in settings.items():
        os.environ[key]=value
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    
