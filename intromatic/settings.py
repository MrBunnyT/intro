from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mi=f*s645ut%rs5#!qo8n=r@c6h7m)2pkvzt7^8dg1%$&$50@9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','www.twitter.com','localhost']
CORS_ALLOWED_ORIGINS = [
    "https://localhost:3000",
    "http://localhost:3000",
    "https://localhost:8000",
    "http://localhost:8000",
]
CORS_URLS_REGEX = r'^/api/.*$'
LOGIN_URL = 'accounts/login'
LOGIN_REDIRECT_URL = 'accounts/profile'
LOGOUT_REDIRECT_URL = ''
MAX_TWEET_LENGTH = 250
MIN_TWEET_LENGTH = 2
TWEET_ACTIONS = ['upvote','downvote','retweet']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # internal django
    'tweets.apps.TweetsConfig',
    # third-party
    'rest_framework',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intromatic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',os.path.join('templates','base'),
            os.path.join('templates','components'),
            os.path.join('templates','react'),
            os.path.join('templates','Home'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'intromatic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'Intromatic',
        'USER':'postgres',
        'PASSWORD':'Bunny123',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]

DEFAULT_AUTHENTICATION_CLASSES = [
    'rest_framework.authentication.SessionAuthentication',
]

DEFAULT_RENDERER_CLASSES = [
    'rest_framework.renderers.JSONRenderer'
]

if DEBUG:
    DEFAULT_RENDERER_CLASSES+= ['rest_framework.renderers.BrowsableAPIRenderer',]
    DEFAULT_AUTHENTICATION_CLASSES += ['intromatic.rest_api.dev.DevAuth']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : DEFAULT_AUTHENTICATION_CLASSES,
    'DEFAULT_RENDERER_CLASSES' : DEFAULT_RENDERER_CLASSES
}

