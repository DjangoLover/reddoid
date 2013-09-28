import sys

from .base import *
from .twitter import *
from .google_plus import *

import dj_database_url


DATABASES = {'default': dj_database_url.config(default='postgres://reddoid:reddoid@localhost/reddoid')}

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb.sqlite3'
    }
