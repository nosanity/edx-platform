from devstack import *

SSO_ENABLED = ENV_TOKENS.get('SSO_ENABLED', False)

SSO_NPOED_URL = ''

if SSO_ENABLED:
    SSO_NPOED_URL = ENV_TOKENS.get('SSO_NPOED_URL', 'http://sso.local.se:8081')
    SSO_API_URL = '%s/api-edx/' % SSO_NPOED_URL
    SSO_API_TOKEN = ENV_TOKENS.get('SSO_API_TOKEN', '123456')

    SOCIAL_AUTH_EXCLUDE_URL_PATTERN = r'^/admin'
    SOCIAL_AUTH_LOGOUT_URL = '%s/logout/' % SSO_NPOED_URL
    SOCIAL_AUTH_RAISE_EXCEPTIONS = True
    # We should login always with npoed-sso. There is specific backend for cms
    # from sso_edx_npoed.backends.npoed import NpoedBackendCMS
    # NpoedBackendCMS.name
    SSO_NPOED_BACKEND_NAME = 'sso_npoed_cms-oauth2'
    LOGIN_URL = '/auth/login/%s/' % SSO_NPOED_BACKEND_NAME

    MIDDLEWARE_CLASSES += ('sso_edx_npoed.middleware.SeamlessAuthorization',)

    ROOT_URLCONF = 'sso_edx_npoed.cms_urls'

    FEATURES['ENABLE_THIRD_PARTY_AUTH'] = True
    THIRD_PARTY_AUTH_BACKENDS = [
        'sso_edx_npoed.backends.npoed.NpoedBackend',
        'sso_edx_npoed.backends.npoed.NpoedBackendCMS',
    ]
    AUTHENTICATION_BACKENDS = THIRD_PARTY_AUTH_BACKENDS + list(AUTHENTICATION_BACKENDS)

    SOCIAL_AUTH_PIPELINE_TIMEOUT = 30

    # Add extra dir for mako templates finder
    NPOED_MAKO_TEMPLATES = ['/edx/app/edxapp/venvs/edxapp/src/sso-edx-npoed/sso_edx_npoed/templates/cms', ]

    MAKO_TEMPLATES['main'] = NPOED_MAKO_TEMPLATES + MAKO_TEMPLATES['main']

# video manager
EVMS_URL = 'https://evms.test.npoed.ru'
EVMS_API_KEY = 'xxxxxxxxxxxxxxxxxx'

FEATURES['PROCTORED_EXAMS_ATTEMPT_DELETE'] = True

FEATURES['EVMS_TURN_ON'] = False
if FEATURES['EVMS_TURN_ON']:
    FEATURES['EVMS_QUALITY_CONTROL_ON'] = True
    INSTALLED_APPS += (
        # Api extension for openedu
        'video_evms',
    )

FEATURES['ENABLE_SPECIAL_EXAMS'] = True

FEATURES['ENABLE_CMS_API'] = False
if FEATURES['ENABLE_CMS_API']:
    INSTALLED_APPS += (
        'open_edx_api_extension_cms',
    )

PROCTORING_BACKEND_PROVIDERS = {
    "dummy": {
        "class": "edx_proctoring.backends.null.NullBackendProvider",
        "options": {},
        "settings": {}
    },
    "EXAMUS": {
        "class": "examus.backends.examus.ExamusBackendProvider",
        "options": {
            "crypto_key": "123456789012345678901234",
            "exam_register_endpoint": "{add endpoint here}",
            "exam_sponsor": "Examus",
            "organization": "NPOED",
            "secret_key": "{add SoftwareSecure secret key}",
            "secret_key_id": "{add SoftwareSecure secret key id}",
            "software_download_url": "https://chrome.google.com/webstore/detail/examus/apippgiggejegjpimfjnaigmanampcjg"
        },
        "settings": {
            "LINK_URLS": {
                "contact_us": "{add link here}",
                "faq": "{add link here}",
                "online_proctoring_rules": "{add link here}",
                "tech_requirements": "{add link here}"
            }
        }
    },
    "ITMO": {
        "class": "itmo.backends.itmo.ItmoBackendProvider",
        "options": {
            "crypto_key": "{add key here}",
            "exam_register_endpoint": "{add endpoint here}",
            "exam_sponsor": "ITMO",
            "organization": "org_name",
            "secret_key": "{add key here}",
            "secret_key_id": "{add id here}",
            "software_download_url": "https://de.ifmo.ru:8443/dist/"
        },
        "settings": {
            "LINK_URLS": {
                "contact_us": "{add link here}",
                "faq": "{add link here}",
                "online_proctoring_rules": "{add link here}",
                "tech_requirements": "{add link here}"
            }
        }
    },
    "WEB_ASSISTANT": {
        "class": "npoed.backends.assistant.NPOEDBackendProvider",
        "options": {
            "crypto_key": "123456789012345678901234",
            "exam_register_endpoint": "https://proctor.local.se:8002/api/exam_register/",
            "exam_sponsor": "Hobo",
            "organization": "HoboHome",
            "secret_key": "hobo_secret_key!",
            "secret_key_id": "hobo_secret_key_id",
            "software_download_url": "{add link here}"
        },
        "settings": {
            "LINK_URLS": {
                "contact_us": "{add link here}",
                "faq": "{add link here}",
                "online_proctoring_rules": "{add link here}",
                "tech_requirements": "{add link here}"
            }
        }
    }
}

COPYRIGHT_YEAR = "2018"

INSTALLED_APPS += ('npoed_grading_features',)
FEATURES["ENABLE_GRADING_FEATURES"] = True
VERTICAL_GRADING_DEFAULT = True

