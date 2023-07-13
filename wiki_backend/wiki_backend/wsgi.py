"""
WSGI config for wiki_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import json

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki_backend.settings')
settings = json.load(open((os.path.join('.config','settings.json')),'r'))
for key,value in settings.items():
    os.environ[key]=value

application = get_wsgi_application()
