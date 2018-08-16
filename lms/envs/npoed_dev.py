from django.utils.translation import ugettext_lazy as _

from devstack import *

ORA2_FILEUPLOAD_BACKEND = 'filesystem'
USERS_WITH_SPECIAL_PERMS_IDS = []
FEATURES['ENABLE_SPECIAL_EXAMS'] = True

SSO_ENABLED = ENV_TOKENS.get("SSO_ENABLED", True)
PLP_ENABLED = ENV_TOKENS.get("PLP_ENABLED", False)

PLP_URL = ""
SSO_NPOED_URL = ""

if SSO_ENABLED:
    SSO_NPOED_URL = ENV_TOKENS.get("SSO_NPOED_URL", 'http://sso.local.se:8081')
    SSO_API_URL = '%s/api-edx/' % SSO_NPOED_URL
    SSO_API_TOKEN = ENV_TOKENS.get("SSO_API_TOKEN", '123456')

    SOCIAL_AUTH_EXCLUDE_URL_PATTERN = r'^/admin'
    SOCIAL_AUTH_LOGOUT_URL = '%s/logout/' % SSO_NPOED_URL
    SOCIAL_AUTH_RAISE_EXCEPTIONS = True

    # We should login always with npoed-sso
    SSO_NPOED_BACKEND_NAME = 'sso_npoed-oauth2'
    LOGIN_URL = '/auth/login/%s/' % SSO_NPOED_BACKEND_NAME

    FEATURES['ENABLE_THIRD_PARTY_AUTH'] = True
    THIRD_PARTY_AUTH_BACKENDS = [
        'sso_edx_npoed.backends.npoed.NpoedBackend',
        'sso_edx_npoed.backends.npoed.NpoedBackendCMS'
    ]
    AUTHENTICATION_BACKENDS = THIRD_PARTY_AUTH_BACKENDS + list(AUTHENTICATION_BACKENDS)

    MIDDLEWARE_CLASSES += ('sso_edx_npoed.middleware.SeamlessAuthorization',)

    ROOT_URLCONF = 'sso_edx_npoed.lms_urls'

if SSO_ENABLED and PLP_ENABLED:
    PLP_URL = ENV_TOKENS.get("PLP_URL", 'http://plp.local.se:8080')
    PLP_API_KEY = ENV_TOKENS.get("PLP_API_KEY", '123456')
    PLP_BAN_ON = True
    FEATURES['ICALENDAR_DUE_API'] = True
    MIDDLEWARE_CLASSES += ('sso_edx_npoed.middleware.PLPRedirection',)

FEATURES['PROCTORED_EXAMS_ATTEMPT_DELETE'] = True

NPOED_MAKO_TEMPLATES = ["/edx/app/edxapp/venvs/edxapp/src/sso-edx-npoed/sso_edx_npoed/templates/lms", ]

# video manager
EVMS_URL = 'https://evms.test.npoed.ru'
EVMS_API_KEY = 'xxxxxxxxxxxxxxxxxx'

INSTALLED_APPS += (
    # Api extension for openedu
    'open_edx_api_extension',
    #'video_evms',
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
PROCTORING_BACKEND_PROVIDERS = AUTH_TOKENS.get("PROCTORING_BACKEND_PROVIDERS", PROCTORING_BACKEND_PROVIDERS)

COURSE_MODE_DEFAULTS = {
    'bulk_sku': None,
    'currency': 'usd',
    'description': None,
    'expiration_datetime': None,
    'min_price': 0,
    'name': _('Honor'),
    'sku': None,
    'slug': 'audit',
    'suggested_prices': '',
}

COPYRIGHT_YEAR = "2018"
PAID_COURSE_REGISTRATION_CURRENCY = ['rub', u"\u20BD"]
FEATURES['ENABLE_SOFTWARE_SECURE_FAKE'] = True

INSTALLED_APPS += ('npoed_grading_features',)
FEATURES["ENABLE_GRADING_FEATURES"] = True
VERTICAL_GRADING_DEFAULT = True
