from tp import *

import os


## Env
PLATFORM_BASE_DOMAIN = os.getenv('PLATFORM_BASE_DOMAIN', 'example.com')
PLATFORM_SCHEME = os.getenv('PLATFORM_SCHEME', 'https')
BUGS_EMAIL = os.getenv('BUGS_EMAIL', 'bugs@{}'.format(PLATFORM_BASE_DOMAIN))
BULK_EMAIL_DEFAULT_FROM_EMAIL = os.getenv('BULK_EMAIL_DEFAULT_FROM_EMAIL', 'bulk@{}'.format(PLATFORM_BASE_DOMAIN))

CACHES = {
    "celery": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "celery",
        "LOCATION": [
            os.getenv('CACHES__celery__LOCATION', '127.0.0.1:11211')
        ],
        "TIMEOUT": 7200
    },
    "configuration": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "edx",
        "LOCATION": [
            os.getenv('CACHES__configuration__LOCATION', '127.0.0.1:11211')
        ]
    },
    "course_structure_cache": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "course_structure",
        "LOCATION": [
            os.getenv('CACHES__course_structure_cache__LOCATION', '127.0.0.1:11211')
        ],
        "TIMEOUT": 7200
    },
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "default",
        "LOCATION": [
            os.getenv('CACHES__default__LOCATION', '127.0.0.1:11211')
        ],
        "VERSION": "1"
    },
    "general": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "general",
        "LOCATION": [
            os.getenv('CACHES__general__LOCATION', '127.0.0.1:11211')
        ]
    },
    "mongo_metadata_inheritance": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "mongo_metadata_inheritance",
        "LOCATION": [
            os.getenv('CACHES__mongo_metadata_inheritance__LOCATION', '127.0.0.1:11211')
        ],
        "TIMEOUT": 300
    },
    "ora2_cache": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "ora2",
        "LOCATION": [
            os.getenv('CACHES__ora2_cache__LOCATION', '127.0.0.1:11211')
        ]
    },
    "staticfiles": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "edx_general",
        "LOCATION": [
            os.getenv('CACHES__staticfiles__LOCATION', '127.0.0.1:11211')
        ]
    }
}


CELERY_BROKER_HOSTNAME = os.getenv('CELERY_BROKER_HOSTNAME', CELERY_BROKER_HOSTNAME if 'CELERY_BROKER_HOSTNAME' in locals() else '127.0.0.1')
CELERY_BROKER_TRANSPORT = os.getenv('CELERY_BROKER_TRANSPORT', CELERY_BROKER_TRANSPORT if 'CELERY_BROKER_TRANSPORT' in locals() else 'amqp')
CELERY_BROKER_USE_SSL = str(os.getenv('CELERY_BROKER_USE_SSL', CELERY_BROKER_USE_SSL if 'CELERY_BROKER_USE_SSL' in locals() else False)) == 'True'
CELERY_BROKER_VHOST = os.getenv('CELERY_BROKER_VHOST', CELERY_BROKER_VHOST if 'CELERY_BROKER_VHOST' in locals() else '')
CMS_BASE = os.getenv('CMS_BASE', '{}.{}'.format(os.getenv('SUB_DOMAIN_STUDIO', 'studio'), PLATFORM_BASE_DOMAIN))

COMMENTS_SERVICE_KEY = os.getenv('COMMENTS_SERVICE_KEY', COMMENTS_SERVICE_KEY if 'COMMENTS_SERVICE_KEY' in locals() else '')
COMMENTS_SERVICE_URL = os.getenv('COMMENTS_SERVICE_URL', COMMENTS_SERVICE_URL if 'COMMENTS_SERVICE_URL' in locals() else 'http://localhost:18080')
COMPREHENSIVE_THEME_DIR = os.getenv('COMPREHENSIVE_THEME_DIR', COMPREHENSIVE_THEME_DIR if 'COMPREHENSIVE_THEME_DIR' in locals() else '/edx/app/edxapp/themes')

CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', 'contact@{}'.format(PLATFORM_BASE_DOMAIN))
DEFAULT_FEEDBACK_EMAIL = os.getenv('DEFAULT_FEEDBACK_EMAIL', 'feedback@{}'.format(PLATFORM_BASE_DOMAIN))
DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE', DEFAULT_FILE_STORAGE if 'DEFAULT_FILE_STORAGE' in locals() else 'django.core.files.storage.FileSystemStorage')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', 'email@{}'.format(PLATFORM_BASE_DOMAIN))
DEFAULT_SITE_THEME = os.getenv('DEFAULT_SITE_THEME', DEFAULT_SITE_THEME if 'DEFAULT_SITE_THEME' in locals() else '')

MAIL_BACKEND = os.getenv('EMAIL_BACKEND', EMAIL_BACKEND if 'EMAIL_BACKEND' in locals() else 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', EMAIL_HOST if 'EMAIL_HOST' in locals() else '127.0.0.1')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', EMAIL_PORT if 'EMAIL_PORT' in locals() else 25))
ENABLE_COMPREHENSIVE_THEMING = str(os.getenv('ENABLE_COMPREHENSIVE_THEMING', ENABLE_COMPREHENSIVE_THEMING if 'ENABLE_COMPREHENSIVE_THEMING' in locals() else False)) == 'True'
EVMS_URL = os.getenv('EVMS_URL', EVMS_URL if 'EVMS_URL' in locals() else 'http://localhost')

FEATURES['ALLOW_ALL_ADVANCED_COMPONENTS'] = str(os.getenv('FEATURES__ALLOW_ALL_ADVANCED_COMPONENTS', True)) == 'True'
FEATURES['ALLOW_COURSE_STAFF_GRADE_DOWNLOADS'] = str(os.getenv('FEATURES__ALLOW_COURSE_STAFF_GRADE_DOWNLOADS', False)) == 'True'
FEATURES['ENABLE_DISCUSSION_HOME_PANEL'] = str(os.getenv('FEATURES__ENABLE_DISCUSSION_HOME_PANEL', True)) == 'True'
FEATURES['ENABLE_DISCUSSION_SERVICE'] = str(os.getenv('FEATURES__ENABLE_DISCUSSION_SERVICE', True)) == 'True'
FEATURES['ENABLE_GRADE_DOWNLOADS'] = str(os.getenv('FEATURES__ENABLE_GRADE_DOWNLOADS', True)) == 'True'
FEATURES['ENABLE_OAUTH2_PROVIDER'] = str(os.getenv('FEATURES__ENABLE_OAUTH2_PROVIDER', True)) == 'True'
FEATURES['ENABLE_PROCTORED_EXAMS'] = str(os.getenv('FEATURES__ENABLE_PROCTORED_EXAMS', True)) == 'True'
FEATURES['ENABLE_SPECIAL_EXAMS'] = str(os.getenv('FEATURES__ENABLE_SPECIAL_EXAMS', True)) == 'True'
FEATURES['ENABLE_SYSADMIN_DASHBOARD'] = str(os.getenv('FEATURES__ENABLE_SYSADMIN_DASHBOARD', False)) == 'True'
FEATURES['ENABLE_THIRD_PARTY_AUTH'] = str(os.getenv('FEATURES__ENABLE_THIRD_PARTY_AUTH', True)) == 'True'
FEATURES['EVMS_QUALITY_CONTROL_ON'] = str(os.getenv('FEATURES__AEVMS_QUALITY_CONTROL_ON', False)) == 'True'
FEATURES['EVMS_TURN_ON'] = str(os.getenv('FEATURES__EVMS_TURN_ON', False)) == 'True'
FEATURES['INDIVIDUAL_DUE_DATES'] = str(os.getenv('FEATURES__INDIVIDUAL_DUE_DATES', True)) == 'True'
FEATURES['USE_CUSTOM_THEME'] = str(os.getenv('FEATURES__USE_CUSTOM_THEME', False)) == 'True'
FEATURES['USE_LANGUAGE_FROM_COURSE_SETTINGS'] = str(os.getenv('FEATURES__USE_LANGUAGE_FROM_COURSE_SETTINGS', False)) == 'True'

FILE_UPLOAD_STORAGE_BUCKET_NAME = os.getenv('FILE_UPLOAD_STORAGE_BUCKET_NAME', FILE_UPLOAD_STORAGE_BUCKET_NAME if 'FILE_UPLOAD_STORAGE_BUCKET_NAME' in locals() else '')
FILE_UPLOAD_STORAGE_PREFIX = os.getenv('FILE_UPLOAD_STORAGE_PREFIX', FILE_UPLOAD_STORAGE_PREFIX if 'FILE_UPLOAD_STORAGE_PREFIX' in locals() else 'submissions_attachments')
FOOTER_ORGANIZATION_IMAGE = os.getenv('FOOTER_ORGANIZATION_IMAGE', FOOTER_ORGANIZATION_IMAGE if 'FOOTER_ORGANIZATION_IMAGE' in locals() else 'images/logo.png')
GITHUB_REPO_ROOT = os.getenv('GITHUB_REPO_ROOT', GITHUB_REPO_ROOT if 'GITHUB_REPO_ROOT' in locals() else '/edx/var/edxapp/data')

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', LANGUAGE_CODE if 'LANGUAGE_CODE' in locals() else 'ru')
LMS_BASE = os.getenv('LMS_BASE', '{}.{}'.format(os.getenv('SUB_DOMAIN_LMS', 'courses'), PLATFORM_BASE_DOMAIN))
LMS_ROOT_URL = os.getenv('LMS_ROOT_URL', '{}://{}'.format(PLATFORM_SCHEME, LMS_BASE))
LOCAL_LOGLEVEL = os.getenv('LOCAL_LOGLEVEL', LOCAL_LOGLEVEL if 'LOCAL_LOGLEVEL' in locals() else 'INFO')
LOGGING_ENV = os.getenv('LOGGING_ENV', LOGGING_ENV if 'LOGGING_ENV' in locals() else 'sandbox')
LOG_DIR = os.getenv('LOG_DIR', LOG_DIR if 'LOG_DIR' in locals() else '/edx/var/logs/edx')
MEDIA_ROOT = os.getenv('MEDIA_ROOT', MEDIA_ROOT if 'MEDIA_ROOT' in locals() else '/edx/var/edxapp/media/')
MEDIA_URL = os.getenv('MEDIA_URL', MEDIA_URL if 'MEDIA_URL' in locals() else '/media/')

TP_MAKO_TEMPLATES = os.getenv('TP_MAKO_TEMPLATES_LMS', '/edx/app/edxapp/venv/src/sso-edx-tp/sso_edx_tp/templates/lms')
TP_MAKO_TEMPLATES = TP_MAKO_TEMPLATES.split(',')
MAKO_TEMPLATES['main'] = TP_MAKO_TEMPLATES + MAKO_TEMPLATES['main']

OAUTH_OIDC_ISSUER = os.getenv('OAUTH_OIDC_ISSUER', '{}/oauth2'.format(LMS_ROOT_URL))

ORA2_FILEUPLOAD_BACKEND = os.getenv('ORA2_FILEUPLOAD_BACKEND', ORA2_FILEUPLOAD_BACKEND if 'ORA2_FILEUPLOAD_BACKEND' in locals() else 'filesystem')
ORA2_FILE_PREFIX = os.getenv('ORA2_FILE_PREFIX', ORA2_FILE_PREFIX if 'ORA2_FILE_PREFIX' in locals()else 'ora2')

PLATFORM_NAME = os.getenv('PLATFORM_NAME', locals().get('PLATFORM_NAME'))
PLP_URL = os.getenv('PLP_URL', '{}://{}'.format(PLATFORM_SCHEME, PLATFORM_BASE_DOMAIN))
PLP_BAN_ON = os.getenv('PLP_BAN_ON', PLP_BAN_ON if 'PLP_BAN_ON' in locals() else False)

PROCTORING_SETTINGS = {
    "ALLOW_REVIEW_UPDATES": True,
    "CLIENT_TIMEOUT": 383,
    "LINK_URLS": {
        "contact_us": "/feedback/",
        "faq": "/proctoring/",
        "online_proctoring_rules": "/proctoring/",
        "tech_requirements": "/systemcheck/"
    },
    "REQUIRE_FAILURE_SECOND_REVIEWS": False,
    "SOFTWARE_SECURE_CLIENT_TIMEOUT": 383
}

PRESS_EMAIL = os.getenv('PRESS_EMAIL', 'press@{}'.format(PLATFORM_BASE_DOMAIN))
SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'server@{}'.format(PLATFORM_BASE_DOMAIN))

SESSION_COOKIE_DOMAIN = os.getenv('SESSION_COOKIE_DOMAIN', locals().get('SESSION_COOKIE_DOMAIN'))
SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME', SESSION_COOKIE_NAME if 'SESSION_COOKIE_NAME' in locals() else 'sessionid')

SITE_NAME = os.getenv('SITE_NAME', LMS_ROOT_URL)

SSO_TP_URL = os.getenv('SSO_TP_URL', '{}://{}.{}'.format(PLATFORM_SCHEME, os.getenv('SUB_DOMAIN_SSO', 'sso'), PLATFORM_BASE_DOMAIN))
if SSO_TP_URL:
    SSO_TP_URL = SSO_TP_URL.rstrip('/')
SSO_API_URL = '%s/api-edx/' % SSO_TP_URL
SOCIAL_AUTH_LOGOUT_URL = '%s/logout/' % SSO_TP_URL

STATIC_ROOT_BASE = os.getenv('STATIC_ROOT_BASE', STATIC_ROOT_BASE if 'STATIC_ROOT_BASE' in locals() else '/edx/var/edxapp/staticfiles')
STATIC_URL_BASE = os.getenv('STATIC_ROOT_URL', STATIC_URL_BASE if 'STATIC_URL_BASE' in locals() else '/static/')


TECH_SUPPORT_EMAIL = os.getenv('TECH_SUPPORT_EMAIL', 'tech@{}'.format(PLATFORM_BASE_DOMAIN))
THEME_NAME = os.getenv('THEME_NAME', locals().get('THEME_NAME'))

THIRD_PARTY_AUTH_BACKENDS_DEFAULT = locals().get('THIRD_PARTY_AUTH_BACKENDS', [])

THIRD_PARTY_AUTH_BACKENDS_OS = []
THIRD_PARTY_AUTH_BACKENDS_LMS = os.getenv('THIRD_PARTY_AUTH_BACKENDS_LMS')
if THIRD_PARTY_AUTH_BACKENDS_LMS:
    THIRD_PARTY_AUTH_BACKENDS_OS.append(THIRD_PARTY_AUTH_BACKENDS_LMS)
THIRD_PARTY_AUTH_BACKENDS_CMS = os.getenv('THIRD_PARTY_AUTH_BACKENDS_CMS')
if THIRD_PARTY_AUTH_BACKENDS_CMS:
    THIRD_PARTY_AUTH_BACKENDS_OS.append(THIRD_PARTY_AUTH_BACKENDS_CMS)

THIRD_PARTY_AUTH_BACKENDS = THIRD_PARTY_AUTH_BACKENDS_OS if THIRD_PARTY_AUTH_BACKENDS_OS else THIRD_PARTY_AUTH_BACKENDS_DEFAULT

TIME_ZONE = os.getenv('TIME_ZONE', locals().get('TIME_ZONE'))
TIME_ZONE_DISPLAYED_FOR_DEADLINES = os.getenv('TIME_ZONE_DISPLAYED_FOR_DEADLINES', locals().get('TIME_ZONE_DISPLAYED_FOR_DEADLINES'))
UNIVERSITY_EMAIL = os.getenv('UNIVERSITY_EMAIL', 'university@{}'.format(PLATFORM_BASE_DOMAIN))

WIKI_ENABLED = os.getenv('WIKI_ENABLED', WIKI_ENABLED if 'WIKI_ENABLED' in locals() else True)


##Auth
CONTENTSTORE = {
    "ADDITIONAL_OPTIONS": {},
    "DOC_STORE_CONFIG": {
        "collection": "modulestore",
        "connectTimeoutMS": 2000,
        "db": "edxapp",
        "host": [
            os.getenv('CONTENTSTORE__DOC_STORE_CONFIG__host', '127.0.0.1')
        ],
        "password": os.getenv('CONTENTSTORE__DOC_STORE_CONFIG__password', os.getenv('EDX_MONGODB_DEFAULT_PASSWORD', '')),
        "port": 27017,
        "socketTimeoutMS": 3000,
        "ssl": False,
        "user": "edxapp"
    },
    "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
    "OPTIONS": {
        "db": "edxapp",
        "host": [
            os.getenv('CONTENTSTORE__OPTIONS__host', '127.0.0.1')
        ],
        "password": os.getenv('CONTENTSTORE__OPTIONS__password', os.getenv('EDX_MONGODB_DEFAULT_PASSWORD', '')),
        "port": 27017,
        "ssl": False,
        "user": "edxapp"
    }
}
CELERY_BROKER_USER = os.getenv('CELERY_BROKER_USER', CELERY_BROKER_USER if 'CELERY_BROKER_USER' in locals() else 'celery')

CELERY_BROKER_PASSWORD = os.getenv('CELERY_BROKER_PASSWORD', CELERY_BROKER_PASSWORD if 'CELERY_BROKER_PASSWORD' in locals() else '')

BROKER_URL = "{0}://{1}:{2}@{3}/{4}".format(CELERY_BROKER_TRANSPORT,
                                            CELERY_BROKER_USER,
                                            CELERY_BROKER_PASSWORD,
                                            CELERY_BROKER_HOSTNAME,
                                            CELERY_BROKER_VHOST)

DATABASES = {
    "default": {
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 0,
        "ENGINE": os.getenv('DATABASES__default__ENGINE', "django.db.backends.mysql"),
        "HOST": os.getenv('DATABASES__default__HOST', '127.0.0.1'),
        "NAME": "edxapp",
        "PASSWORD": os.getenv('DATABASES__default__password', os.getenv('EDX_DATABASES_DEFAULT_PASSWORD', '')),
        "PORT": "3306",
        "USER": "edxapp001"
    },
    "read_replica": {
        "CONN_MAX_AGE": 0,
        "ENGINE": os.getenv('DATABASES__read_replica__ENGINE', "django.db.backends.mysql"),
        "HOST": os.getenv('DATABASES__read_replica__HOST', '127.0.0.1'),
        "NAME": "edxapp",
        "PASSWORD": os.getenv('DATABASES__read_replica__password', os.getenv('EDX_DATABASES_DEFAULT_PASSWORD', '')),
        "PORT": "3306",
        "USER": "edxapp001"
    },
    "student_module_history": {
        "CONN_MAX_AGE": 0,
        "ENGINE": os.getenv('DATABASES__student_module_history__ENGINE', "django.db.backends.mysql"),
        "HOST": os.getenv('DATABASES__student_module_history__HOST', '127.0.0.1'),
        "NAME": "edxapp_csmh",
        "PASSWORD": os.getenv('DATABASES__student_module_history__password', os.getenv('EDX_DATABASES_DEFAULT_PASSWORD', '')),
        "PORT": "3306",
        "USER": "edxapp001"
    }
}

DOC_STORE_CONFIG = {
    "collection": "modulestore",
    "connectTimeoutMS": 2000,
    "db": "edxapp",
    "host": [
        os.getenv('DOC_STORE_CONFIG__host', '127.0.0.1')
    ],
    "password": os.getenv('DOC_STORE_CONFIG__password', os.getenv('EDX_MONGODB_DEFAULT_PASSWORD', '')),
    "port": 27017,
    "socketTimeoutMS": 3000,
    "ssl": False,
    "user": "edxapp"
}

DEFAULT_FILE_STORAGE = os.getenv('DEFAULT_FILE_STORAGE', DEFAULT_FILE_STORAGE if 'DEFAULT_FILE_STORAGE' in locals() else 'django.core.files.storage.FileSystemStorage')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', locals().get('EMAIL_HOST_PASSWORD'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', locals().get('EMAIL_HOST_USER'))

GRADES_DOWNLOAD = {                                                                                                                                                
    "BUCKET": os.getenv('GRADES_DOWNLOAD_BUCKET', ''),                                                                                                                                                     
    "CUSTOM_DOMAIN": os.getenv('GRADES_DOWNLOAD_CUSTOM_DOMAIN', ''),                                                                                                                                              
    "ROOT_PATH": os.getenv('GRADES_DOWNLOAD_ROOT_PATH', ''),                                                                                                                                                  
    "STORAGE_CLASS": os.getenv('GRADES_DOWNLOAD_STORAGE_CLASS', 'django.core.files.storage.FileSystemStorage'),                                                                                                   
    "STORAGE_KWARGS": {                                                                                                                                               
        "location": os.getenv('GRADES_DOWNLOAD_location', '/edx/var/edxapp/grades')                                                                                                                              
    },                                                                                                                                                                
    "STORAGE_TYPE": os.getenv('GRADES_DOWNLOAD_STORAGE_TYPE', '')                                                                                                                                                
}

MODULESTORE = {
    "default": {
        "ENGINE": "xmodule.modulestore.mixed.MixedModuleStore",
        "OPTIONS": {
            "mappings": {},
            "stores": [
                {
                    "DOC_STORE_CONFIG": {
                        "collection": "modulestore",
                        "connectTimeoutMS": 2000,
                        "db": "edxapp",
                        "host": [
                            os.getenv('split__MODULESTORE__default__OPTIONS__stores__DOC_STORE_CONFIG__host', '127.0.0.1')
                        ],
                        "password": os.getenv('split__MODULESTORE__default__OPTIONS__stores__DOC_STORE_CONFIG__password',
                                              os.getenv('EDX_MONGODB_DEFAULT_PASSWORD', '')),
                        "port": 27017,
                        "socketTimeoutMS": 3000,
                        "ssl": False,
                        "user": "edxapp"
                    },
                    "ENGINE": "xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore",
                    "NAME": "split",
                    "OPTIONS": {
                        "default_class": "xmodule.hidden_module.HiddenDescriptor",
                        "fs_root": "/edx/var/edxapp/data",
                        "render_template": "edxmako.shortcuts.render_to_string"
                    }
                },
                {
                    "DOC_STORE_CONFIG": {
                        "collection": "modulestore",
                        "connectTimeoutMS": 2000,
                        "db": "edxapp",
                        "host": [
                            os.getenv('draft__MODULESTORE__default__OPTIONS__stores__DOC_STORE_CONFIG__host', '127.0.0.1')
                        ],
                        "password": os.getenv('draft__MODULESTORE__default__OPTIONS__stores__DOC_STORE_CONFIG__password',
                                              os.getenv('EDX_MONGODB_DEFAULT_PASSWORD', '')),
                        "port": 27017,
                        "socketTimeoutMS": 3000,
                        "ssl": False,
                        "user": "edxapp"
                    },
                    "ENGINE": "xmodule.modulestore.mongo.DraftMongoModuleStore",
                    "NAME": "draft",
                    "OPTIONS": {
                        "default_class": "xmodule.hidden_module.HiddenDescriptor",
                        "fs_root": "/edx/var/edxapp/data",
                        "render_template": "edxmako.shortcuts.render_to_string"
                    }
                }
            ]
        }
    }
}

PROCTORING_BACKEND_PROVIDERS = {
    "dummy": {
        "class": "edx_proctoring.backends.null.NullBackendProvider",
        "options": {},
        "settings": {}
    },
    "WEB_ASSISTANT": {
        "class": "tp.backends.assistant.TPBackendProvider",
        "options": {
            "crypto_key": os.getenv('WEB_ASSISTANT__crypto_key', ''),
            "exam_register_endpoint": os.getenv('WEB_ASSISTANT__exam_register_endpoint', 'http://localhost'),
            "exam_sponsor": "Hobo",
            "organization": "HoboHome",
            "secret_key": os.getenv('WEB_ASSISTANT__secret_key', ''),
            "secret_key_id": os.getenv('WEB_ASSISTANT__secret_key_id', ''),
            "software_download_url": "https://test.tp.ru/systemcheck/"
        },
        "settings": {
            "LINK_URLS": {
                "contact_us": os.getenv('WEB_ASSISTANT__contact_us', 'http://localhost/feedback'),
                "faq": os.getenv('WEB_ASSISTANT__faq', 'http://localhost/proctoring/'),
                "online_proctoring_rules": os.getenv('WEB_ASSISTANT__online_proctoring_rules', 'http://localhost/rules/'),
                "tech_requirements": os.getenv('WEB_ASSISTANT__tech_requirements', 'http://localhost/systemcheck/')
            }
        }
    }
}
    
# ==== Raven ====
RAVEN_DSN = os.getenv('DSN')
if RAVEN_DSN:
    RAVEN_CONFIG = {
        'dsn': RAVEN_DSN,
        'release': os.getenv('RAVEN_CONFIG__tags__release', ''),
        #'release': raven.fetch_git_sha(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'tags': {
            'env': os.getenv('RAVEN_CONFIG__tags__env', '')
    }
    }
    try:
        from raven.transport.requests import RequestsHTTPTransport
        from raven import Client
        RAVEN_CONFIG['transport'] = RequestsHTTPTransport
        RAVEN_CLIENT = Client(**RAVEN_CONFIG)
    except ImportError:
        print 'could not enable Raven!'
# =====================================

EDX_API_KEY = os.getenv('EDX_API_KEY', EDX_API_KEY if 'EDX_API_KEY' in locals() else '')
PLP_API_KEY = os.getenv('PLP_API_KEY', PLP_API_KEY if 'PLP_API_KEY' in locals() else '')
SSO_API_KEY = os.getenv('SSO_API_KEY', SSO_API_KEY if 'SSO_API_KEY' in locals() else '')
SSO_API_TOKEN = os.getenv('SSO_API_TOKEN', SSO_API_TOKEN if 'SSO_API_TOKEN' in locals() else '')

REDIRECT_IS_HTTPS = str(os.getenv('REDIRECT_IS_HTTPS', True)) == 'True'

VERIFY_STUDENT = {
    "DAYS_GOOD_FOR": 365,
    "EXPIRING_SOON_WINDOW": 28,
    "SOFTWARE_SECURE": {
        "API_ACCESS_KEY": "BBBBBBBBBBBBBBBBBBBB",
        "API_SECRET_KEY": "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC",
        "API_URL": os.getenv('VERIFY_STUDENT__API_URL', 'https://localhost/verify_student/fake_endpoint'),
        "AWS_ACCESS_KEY": "FAKEACCESSKEY",
        "AWS_SECRET_KEY": "FAKESECRETKEY",
        "FACE_IMAGE_AES_KEY": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "S3_BUCKET": "fake-bucket"
    }
}

XQUEUE_INTERFACE = {
    'basic_auth': [
        'edx',
        'edx'
    ],
    'django_auth': {
        'password': os.getenv('XQUEUE_INTERFACE__django_auth__password', ''),
        'username': 'lms'
    },
    'url': os.getenv('XQUEUE_INTERFACE__url', 'http://localhost:18040'),
}

SUPERUSER_USERNAME = os.getenv('SUPERUSER_USERNAME', 'admin')
SUPERUSER_EMAIL = os.getenv('SUPERUSER_EMAIL', 'admin@{}'.format('.'.join(SITE_NAME.split('.')[1:]) if len(SITE_NAME.split('.')) > 2 else SITE_NAME))
SUPERUSER_PASSWORD = os.getenv('SUPERUSER_PASSWORD')
