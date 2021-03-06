# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
import os

LANGUAGE_CODE = 'pt-br'
LOCALE_CODE = 'pt_BR'

USE_I18N = True
USE_L10N = True

LOCALE_PATHS = (os.path.join(PROJECT_DIR, 'conf/locale'),)
