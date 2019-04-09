#  Name:    Maoxin Hou,  Xiren Zhou, Yiqian Wang
#  UNI:   mh3895,  xz2754,  yw3225
#  Group Code: MOHA

"""
WSGI config for iotTEMP project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iotTEMP.settings")

application = get_wsgi_application()
