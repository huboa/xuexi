"""
Django settings for fortress_lfzb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#_nm9bqz$5*pony7aoqmlwb2hx2!ssbpyb-2lo^si7xh91i7!h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grant',
    'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (  
        "django.contrib.auth.context_processors.auth",  
        "django.core.context_processors.debug",  
        "django.core.context_processors.i18n",  
        "django.core.context_processors.media",  
        "django.core.context_processors.request"  
    )

ROOT_URLCONF = 'fortress_lfzb.urls'

WSGI_APPLICATION = 'fortress_lfzb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fortress',
        'USER': 'mtimedb',
        'PASSWORD': 'mtimedbpwd',
        'HOST': '10.10.130.7',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

EMAIL_HOST='mail.service.mtime.com'
EMAIL_PORT = 25
EMAIL_HOST_USER='monitor@service.mtime.com'
EMAIL_HOST_PASSWORD='mtime.com'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'jie.wang@mtime.com'

STATIC_URL = '/static/'
TEMPLATE_DIRS = ('/home/mtime/fortress_lfzb/grant/templates',)
LOGIN_URL = '/login/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALL_OPS = ['gang.luo','xiaolong.lv','rubin.wang','shuo.yang','guoli.yang','ruikai.jiang','zhenhong.sun','jiajun.zhu','ya.wang','haijiang.jiang','leo.huang','hailong.sun','qishan.hao','po.shi','haimin.hao','shengchong.zhao','liang.kang']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT' : 600,
    }
}
