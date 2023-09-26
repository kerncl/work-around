import sys
import os
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.core.wsgi import get_wsgi_application


DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG= DEBUG,
    SCRET_KEY = SECRET_KEY,
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

def index(request):
    return HttpResponse('Hello world')

application = get_wsgi_application()

urlpatterns = (
    url(r'^$', index),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)