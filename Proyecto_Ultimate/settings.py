"""
Django settings for Proyecto_Ultimate project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-epgtn3oc%(2tli0ipv_lny2302$#i2oeyt-#gshw)7-t9x(i7*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'proyectos',
    'notificaciones',
    'import_export',
    'ckeditor',
    'django_extensions',
]
JAZZMIN_SETTINGS ={
    
    "user_avatar": 'https://cdn-icons-png.flaticon.com/512/1782/1782950.png',
    "site_header" : 'Construmas S.A DE C.V',
    "welcome_sign": "Sistema / Control De Proyectos",
    "copyright": "Construmas S.A DE C.V",
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "carousel", "auth.group": "carousel"},
    "usermenu_links": [
        {"name": "Pagina Web", "url": "https://construmas.com.sv/", "new_window": False},
        {"model": "auth.user"}
    ],
    "custom_css": "css/main.css",
    "custom_js": "js/main.js",
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

    ],
    "search_model": "proyectos.Agrupaciones",
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-fingerprint",
        "auth.Group": "fas fa-users",
        "notificaciones.Notificacion": "fas fa-envelope",
        "proyectos.Contratista": "fas fa-toolbox",
        "proyectos.Agrupaciones": "fas fa-tasks" ,
        "proyectos.Adicionales": "fas fa-plus"
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-book",
    "default_icon_children": "fas fa-book",
    "related_modal_active": True
    
}
JAZZMIN_SETTINGS["show_ui_builder"] = True


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": True,
    "brand_colour": False,
    "accent": "accent-navy",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-light-navy",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    "actions_sticky_top": False
}




CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'height': 200,
        'width': 400,
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Proyecto_Ultimate.urls'

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

WSGI_APPLICATION = 'Proyecto_Ultimate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'proyectos',
    #     'USER': 'postgres',
    #     'PASSWORD': 'rikyjo11',
    #     'HOST': 'localhost',
    #     'PORT': 5432,
    # }
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


CSRF_USE_SESSIONS = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
DATE_INPUT_FORMATS = ['%d-%m-%Y']

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/El_Salvador'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = './proyectos/static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

