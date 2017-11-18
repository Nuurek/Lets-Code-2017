import dj_database_url

from .base import *


ALLOWED_HOSTS += (
    'officelink.herokuapp.com',
)

database_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': database_from_env
}