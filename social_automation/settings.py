"""
Django settings for social_automation project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ENVIRONMENTS(Enum):
    PROD = "production"
    STAGE = "staging"
    DEV = "development"

ENV_NAME = os.environ.get('ENVIRONMENT', socket.gethostname())
SSL_NOT_REQUIRED = ENV_NAME not in (ENVIRONMENTS.PROD.value, ENVIRONMENTS.DEV.value)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')h^l%09^40w6x9yt%2==+y-r!&vyo1-=41@mrqhi_9-or(02v3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV_NAME != 'production'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social_automation',
	'twitter',
	'facebook',
	'linkedin'
)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social.pipeline.user.create_user',

    # Create the record that associated the social account with this user.
    'social.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social.pipeline.user.user_details',

    # Add the user's avatar
    'tenderbelly.auth_pipeline.add_avatar'
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
)

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

LOGIN_URL = '/login'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = not SSL_NOT_REQUIRED
SOCIAL_AUTH_TRAILING_SLASH = False

SOCIAL_AUTH_RAISE_EXCEPTIONS = True
RAISE_EXCEPTIONS = False

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('GOOGLE_AUTH_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('GOOGLE_AUTH_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['tenderbelly.com', 'spigotlabs.com']
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_EMAILS = ['svvitale@gmail.com', 'mikepeper@gmail.com']
SOCIAL_AUTH_GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'prompt': 'select_account'
}

if not SOCIAL_AUTH_GOOGLE_OAUTH2_KEY or not SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET:
    print("Google OAuth is DISABLED")
else:
    print("Google OAuth is ENABLED")

ROOT_URLCONF = 'social_automation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_automation.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

import dj_database_url  # nopep8
DATABASES = {'default': dj_database_url.config(default='postgres://qitmwmfmutlwqd:Mxbrk9YRZXpnD8cPPuti4zVE-4@ec2-54-204-30-115.compute-1.amazonaws.com:5432/d2745uvcegvacs')}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
# noinspection PyUnresolvedReferences
STATIC_ROOT = os.path.join(BASE_DIR, 'static')   # MEP - not sure why the noinspection is needed...
# noinspection PyUnresolvedReferences
STATICFILES_DIRS = (('js', 'bower_components'),)

# Rollbar Configuration
ROLLBAR_TOKEN = os.environ.get('ROLLBAR_ACCESS_TOKEN')

if ROLLBAR_TOKEN:
    ROLLBAR = {
        'access_token': ROLLBAR_TOKEN,
        'environment': ENV_NAME,
        'branch': 'master',
        'root': BASE_DIR,
    }

    print("Rollbar configured.")
else:
    ROLLBAR = {}
    print("Rollbar NOT configured.")


APPEND_SLASHES = False
