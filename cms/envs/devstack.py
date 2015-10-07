"""
Specific overrides to the base prod settings to make development easier.
"""

from .aws import *  # pylint: disable=wildcard-import, unused-wildcard-import

# Don't use S3 in devstack, fall back to filesystem
del DEFAULT_FILE_STORAGE
MEDIA_ROOT = "/edx/var/edxapp/uploads"

DEBUG = True
USE_I18N = True
TEMPLATE_DEBUG = DEBUG

################################ LOGGERS ######################################

import logging

# Disable noisy loggers
for pkg_name in ['track.contexts', 'track.middleware', 'dd.dogapi']:
    logging.getLogger(pkg_name).setLevel(logging.CRITICAL)

FEATURES['ENABLE_THIRD_PARTY_AUTH'] = True
FEATURES['ENABLE_OAUTH2_PROVIDER'] = True

################################ EMAIL ########################################

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

################################# LMS INTEGRATION #############################

LMS_BASE = "localhost:8000"
FEATURES['PREVIEW_LMS_BASE'] = "preview." + LMS_BASE

########################### PIPELINE #################################

# Skip RequireJS optimizer in development
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

############################# ADVANCED COMPONENTS #############################

# Make it easier to test advanced components in local dev
FEATURES['ALLOW_ALL_ADVANCED_COMPONENTS'] = True

################################# CELERY ######################################

# By default don't use a worker, execute tasks as if they were local functions
CELERY_ALWAYS_EAGER = True

################################ DEBUG TOOLBAR ################################
INSTALLED_APPS += ('debug_toolbar', 'debug_toolbar_mongo')
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'cms.envs.devstack.should_show_debug_toolbar'
}


def should_show_debug_toolbar(_):
    return True  # We always want the toolbar on devstack regardless of IP, auth, etc.


# To see stacktraces for MongoDB queries, set this to True.
# Stacktraces slow down page loads drastically (for pages with lots of queries).
DEBUG_TOOLBAR_MONGO_STACKTRACES = False


################################ MILESTONES ################################
FEATURES['MILESTONES_APP'] = True


################################ ENTRANCE EXAMS ################################
FEATURES['ENTRANCE_EXAMS'] = True

################################ COURSE LICENSES ################################
FEATURES['LICENSING'] = True
# Needed to enable licensing on video modules
XBLOCK_SETTINGS = {
    "VideoDescriptor": {
        "licensing_enabled": True
    }
}

################################ SEARCH INDEX ################################
FEATURES['ENABLE_COURSEWARE_INDEX'] = True
FEATURES['ENABLE_LIBRARY_INDEX'] = True
SEARCH_ENGINE = "search.elastic.ElasticSearchEngine"

########################## Certificates Web/HTML View #######################
FEATURES['CERTIFICATES_HTML_VIEW'] = True

################################# DJANGO-REQUIRE ###############################

# Whether to run django-require in debug mode.
REQUIRE_DEBUG = DEBUG

###############################################################################
# See if the developer has any local overrides.
try:
    from .private import *  # pylint: disable=import-error
except ImportError:
    pass

#####################################################################
# Lastly, run any migrations, if needed.
MODULESTORE = convert_module_store_setting_if_needed(MODULESTORE)

# Dummy secret key for dev
SECRET_KEY = '85920908f28904ed733fe576320db18cabd7b6cd'



















SSO_NPOED_URL = ENV_TOKENS.get('SSO_NPOED_URL') #'http://sso.rnoep.raccoongang.com'

SSO_API_URL = "%s/api-edx/" % SSO_NPOED_URL  #'http://sso.rnoep.raccoongang.com/api-edx/'
SSO_API_TOKEN = AUTH_TOKENS.get('SSO_API_TOKEN') #'b4c2b895087d457b86fc9096f344a687947b70fb'


SOCIAL_AUTH_EXCLUDE_URL_PATTERN = r'^/admin'
SOCIAL_AUTH_LOGOUT_URL = "%s/logout/" % SSO_NPOED_URL #'http://sso.rnoep.raccoongang.com/logout/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = True

MIDDLEWARE_CLASSES += ('sso_edx_npoed.middleware.SeamlessAuthorization', )

# We should login always with npoed-sso. There is specific backend for cms
# from sso_edx_npoed.backends.npoed import NpoedBackendCMS
# NpoedBackendCMS.name
SSO_NPOED_BACKEND_NAME = 'sso_npoed_cms-oauth2'
LOGIN_URL = '/auth/login/%s/' % SSO_NPOED_BACKEND_NAME

# Add extra dir for mako templates finder
# '/edx/app/edxapp/venvs/edxapp/src/npoed-sso-edx-client/sso_edx_npoed/templates')
# NPOED_MAKO_TEMPLATES = ENV_TOKENS.get('NPOED_MAKO_TEMPLATES', [])
NPOED_MAKO_TEMPLATES = [
       "/edx/app/edxapp/venvs/edxapp/src/sso-edx-npoed/sso_edx_npoed/templates"
   ]
#TEMPLATE_DIRS.insert(0, '/edx/app/edxapp/venvs/edxapp/src/npoed-sso-edx-client/sso_edx_npoed')
MAKO_TEMPLATES['main'] = NPOED_MAKO_TEMPLATES + MAKO_TEMPLATES['main']

import datetime
CELERYBEAT_SCHEDULE = {}

##### Third-party auth options ################################################ copied from lms/aws.py
if FEATURES.get('ENABLE_THIRD_PARTY_AUTH'):
    THIRD_PARTY_AUTH_BACKENDS = ENV_TOKENS.get('THIRD_PARTY_AUTH_BACKENDS')

    if THIRD_PARTY_AUTH_BACKENDS:
        AUTHENTICATION_BACKENDS = THIRD_PARTY_AUTH_BACKENDS + list(AUTHENTICATION_BACKENDS)

    # The reduced session expiry time during the third party login pipeline. (Value in seconds)
    SOCIAL_AUTH_PIPELINE_TIMEOUT = ENV_TOKENS.get('SOCIAL_AUTH_PIPELINE_TIMEOUT', 600)

    # third_party_auth config moved to ConfigurationModels. This is for data migration only:
    THIRD_PARTY_AUTH_OLD_CONFIG = AUTH_TOKENS.get('THIRD_PARTY_AUTH', None)

    if ENV_TOKENS.get('THIRD_PARTY_AUTH_SAML_FETCH_PERIOD_HOURS', 24) is not None:
        CELERYBEAT_SCHEDULE['refresh-saml-metadata'] = {
            'task': 'third_party_auth.fetch_saml_metadata',
            'schedule': datetime.timedelta(hours=ENV_TOKENS.get('THIRD_PARTY_AUTH_SAML_FETCH_PERIOD_HOURS', 24)),
        }

EVMS_URL = ENV_TOKENS.get('EVMS_URL')
EVMS_API_KEY = AUTH_TOKENS.get('EVMS_API_KEY')
DEBUG=True
STATICFILES_DIRS = (
    '/edx/var/edxapp/staticfiles',
)
# from django.conf import settings
# for i in dir(settings):
#     if 'static' in i.lower():
#         print i, getattr(settings, i)

# print '----DEBUG', settings.DEBUG