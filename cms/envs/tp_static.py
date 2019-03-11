import os
import json
from .common import *

# due to a bug in simple_history
DATABASES = {
    "default": {
        "ENGINE": "",
    }
}

CONFIG_ROOT = path(os.environ.get('CONFIG_ROOT', ENV_ROOT))
SERVICE_VARIANT = os.environ.get('SERVICE_VARIANT', None)
CONFIG_PREFIX = SERVICE_VARIANT + "." if SERVICE_VARIANT else ""
with open(CONFIG_ROOT / CONFIG_PREFIX + "env.json") as env_file:
    ENV_TOKENS = json.load(env_file)

for app in ENV_TOKENS.get('ADDL_INSTALLED_APPS', []):
    INSTALLED_APPS += (app, )
# FIXME: duplication from tp.py
INSTALLED_APPS += (
    'open_edx_api_extension_cms',
    'video_evms',
)

COMPREHENSIVE_THEME_DIRS = ENV_TOKENS.get('COMPREHENSIVE_THEME_DIRS', COMPREHENSIVE_THEME_DIRS) or []

DEFAULT_GRADING_TYPE = EDX_GRADING_TYPE

LOCALE_PATHS = tuple()
for T in TEMPLATES:
    if T['NAME'] == 'mako':
        T['DIRS'] = MAKO_TEMPLATE_DIRS_BASE
