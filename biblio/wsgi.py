"""
WSGI config for biblio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblio.settings")

from django.core.wsgi import get_wsgi_application
=======
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblio.settings")

>>>>>>> f7544b077d305be9d45ff1551ad65dd9172111dd
application = get_wsgi_application()
