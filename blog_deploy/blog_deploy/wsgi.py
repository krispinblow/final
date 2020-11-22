<<<<<<< HEAD
"""
WSGI config for blog_deploy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_deploy.settings')

application = get_wsgi_application()
=======
"""
WSGI config for blog_deploy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_deploy.settings')

application = get_wsgi_application()
>>>>>>> cee217ef8247483092a4e186f2cbb868d393e645
