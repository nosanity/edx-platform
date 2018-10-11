from aws import *

# ==== Raven ====
RAVEN_CONFIG = AUTH_TOKENS.get('RAVEN_CONFIG', {})
if RAVEN_CONFIG:
    try:
        from raven.transport.requests import RequestsHTTPTransport
        RAVEN_CONFIG['transport'] = RequestsHTTPTransport
        INSTALLED_APPS += ('raven.contrib.django.raven_compat', )
    except ImportError:
        print 'could not enable Raven!'
# ===============

SSO_NPOED_URL = ENV_TOKENS.get('SSO_NPOED_URL', 'http://sso.local.se:8081').rstrip('/')

SSO_API_URL = '%s/api-edx/' % SSO_NPOED_URL
SSO_API_TOKEN = AUTH_TOKENS.get('SSO_API_TOKEN')

SOCIAL_AUTH_EXCLUDE_URL_PATTERN = r'^/admin'
SOCIAL_AUTH_LOGOUT_URL = '%s/logout/' % SSO_NPOED_URL
SOCIAL_AUTH_RAISE_EXCEPTIONS = True

MIDDLEWARE_CLASSES += (
    'sso_edx_npoed.middleware.SeamlessAuthorization',
)

SSO_NPOED_BACKEND_NAME = 'sso_npoed_cms-oauth2'
LOGIN_URL = '/auth/login/%s/' % SSO_NPOED_BACKEND_NAME

PLP_URL = ENV_TOKENS.get('PLP_URL', 'http://plp.local.se:8080').rstrip('/')

NPOED_MAKO_TEMPLATES = ENV_TOKENS.get('NPOED_MAKO_TEMPLATES',
                                      ['/edx/app/edxapp/venvs/edxapp/src/sso-edx-npoed/sso_edx_npoed/templates/cms/'])

MAKO_TEMPLATES['main'] = NPOED_MAKO_TEMPLATES + MAKO_TEMPLATES['main']

# Copy-paste base third party auth settings from lms
##### Third-party auth options ################################################
if FEATURES.get('ENABLE_THIRD_PARTY_AUTH'):
    AUTHENTICATION_BACKENDS = (
        ENV_TOKENS.get('THIRD_PARTY_AUTH_BACKENDS', []) + list(AUTHENTICATION_BACKENDS)
    )

    # The reduced session expiry time during the third party login pipeline. (Value in seconds)
    SOCIAL_AUTH_PIPELINE_TIMEOUT = ENV_TOKENS.get('SOCIAL_AUTH_PIPELINE_TIMEOUT', 600)
    SOCIAL_AUTH_OAUTH_SECRETS = AUTH_TOKENS.get('SOCIAL_AUTH_OAUTH_SECRETS', {})

# Only staff users will have ability to crate course
FEATURES['DISABLE_COURSE_CREATION'] = True


PROCTORING_BACKEND_PROVIDERS = {
    'default': {
        'class': 'edx_proctoring.backends.null.NullBackendProvider',
        'options': {},
    }
}
PROCTORING_BACKEND_PROVIDERS = AUTH_TOKENS.get("PROCTORING_BACKEND_PROVIDERS", PROCTORING_BACKEND_PROVIDERS)
FEATURES['PROCTORED_EXAMS_ATTEMPT_DELETE'] = FEATURES.get('PROCTORED_EXAMS_ATTEMPT_DELETE', False)

EDX_API_KEY = AUTH_TOKENS.get("EDX_API_KEY")

FILE_UPLOAD_STORAGE_BUCKET_NAME = ENV_TOKENS.get('FILE_UPLOAD_STORAGE_BUCKET_NAME', None)

XQUEUE_WAITTIME_BETWEEN_REQUESTS = 5  # seconds

if AUTH_TOKENS.get('AWS_S3_CALLING_FORMAT'):
    AWS_S3_CALLING_FORMAT = AUTH_TOKENS.get('AWS_S3_CALLING_FORMAT')

AWS_STORAGE_BUCKET_NAME = AUTH_TOKENS.get('AWS_STORAGE_BUCKET_NAME', 'edxuploads')


FEATURES['EVMS_TURN_ON'] = False

if FEATURES['EVMS_TURN_ON']:
    INSTALLED_APPS += (
        # Api extension for eduscaled
        'video_evms',
    )
    FEATURES['EVMS_QUALITY_CONTROL_ON'] = True
    EVMS_URL = ENV_TOKENS.get('EVMS_URL', None)
    EVMS_API_KEY = AUTH_TOKENS.get('EVMS_API_KEY', None)

LOCALE_PATHS = (REPO_ROOT + "/eduscaled/npoed_translations", ) + LOCALE_PATHS

ORA_PATH_VENV = 'venvs/edxapp/lib/python2.7/site-packages/openassessment'
ORA_LOCALE_PATH = '{}/{}/locale'.format(PROJECT_ROOT.dirname().dirname(), ORA_PATH_VENV)
LOCALE_PATHS += (ORA_LOCALE_PATH,)

ORA_SRC_PATH_VENV = 'venvs/edxapp/src/ora2/openassessment'
ORA_LOCALE_PATH = '{}/{}/locale'.format(PROJECT_ROOT.dirname().dirname(), ORA_SRC_PATH_VENV)
LOCALE_PATHS += (ORA_LOCALE_PATH,)

PROCTOR_PATH_VENV = "venvs/edxapp/src/edx-proctoring/edx_proctoring"
PROCTOR_LOCALE_PATH = '{}/{}/locale'.format(PROJECT_ROOT.dirname().dirname(), PROCTOR_PATH_VENV)
LOCALE_PATHS += (PROCTOR_LOCALE_PATH,)

COMMENTS_SERVICE_URL = ENV_TOKENS.get('COMMENTS_SERVICE_URL', '')
COMMENTS_SERVICE_KEY = ENV_TOKENS.get('COMMENTS_SERVICE_KEY', '')

COPYRIGHT_YEAR = "2018"

INSTALLED_APPS += ('npoed_grading_features',)
FEATURES["ENABLE_GRADING_FEATURES"] = True
VERTICAL_GRADING_DEFAULT = True

FEATURES['ENABLE_CMS_API'] = True
if FEATURES['ENABLE_CMS_API']:
    INSTALLED_APPS += (
        'open_edx_api_extension_cms',
    )