import os

import dj_database_url

from base import *

# https://devcenter.heroku.com/articles/django#django-settings

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# To set environment variables see config_heroku.sample.sh in root of the project

SOCIAL_AUTH_TWITTER_KEY = os.environ['SOCIAL_AUTH_TWITTER_KEY']
SOCIAL_AUTH_TWITTER_SECRET = os.environ['SOCIAL_AUTH_TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
