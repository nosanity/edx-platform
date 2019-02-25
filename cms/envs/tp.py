from .aws import *

MIDDLEWARE_CLASSES += ('sso_edx_tp.middleware.SeamlessAuthorization',)
CUSTOM_THIRD_PARTY_AUTH_STRATEGY = 'sso_edx_tp.strategy.ConfigurationModelStrategy'

SSO_TP_URL = ENV_TOKENS.get('SSO_TP_URL')
if SSO_TP_URL:
    SSO_TP_URL = SSO_TP_URL.rstrip('/')

SSO_API_URL = '%s/api-edx/' % SSO_TP_URL
SSO_API_TOKEN = AUTH_TOKENS.get('SSO_API_TOKEN')
