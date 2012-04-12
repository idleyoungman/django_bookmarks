import os
import sys

for dir in ['/srv', '/srv/django_bookmarks']:
	sys.path.append(dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_bookmarks.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
