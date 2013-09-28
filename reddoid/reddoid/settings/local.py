from .base import *
from .twitter import *

import dj_database_url

DATABASES = {'default': dj_database_url.config(default='postgres://reddoid:reddoid@localhost/reddoid')}
