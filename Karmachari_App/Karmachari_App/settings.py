from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y^4uzu&71a__gbpf)09^q49ddb8)t6)vd7gj1^=7omqy(mmx^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['7db0-2400-1a00-b030-3a5a-58ba-ca41-b42e-e517.ap.ngrok.io','localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['https://7db0-2400-1a00-b030-3a5a-58ba-ca41-b42e-e517.ap.ngrok.io','https://*.127.0.0.1']



# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fontawesomefree',
    'mainapp',
    'password_reset',
    'calendarr',
    # 'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

ROOT_URLCONF = 'Karmachari_App.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'Karmachari_App.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'karmachari', 
        'USER': 'postgres',
        'PASSWORD': 'useradmin',
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT= os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')


#SMTP CONFIGURATION
EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER='karmachari07@gmail.com'
EMAIL_HOST_PASSWORD='rkugionhlzgwaazl'


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

JAZZMIN_SETTINGS = {
    "show_ui_builder":True,
    "site_title": "Karmachari",
    "site_header":"Karmachari",
    "site_brand": "Karmachari",
    "site_logo": "assets/img/icon32.png",
    "footer_version": False,
    # Relative path to logo for your site, used for login logo (must be present in static files. Defaults to site_logo)
    "login_logo":"assets/img/icon80.png",
    "site_logo_classes": None,
    "welcome_sign": "Welcome to the Karmachari-website",
    "copyright": "Karmachari",
    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "Profile.get_avatar_url",
    "icons": {
        "auth":"fas fa-users-cog",
        "auth.user":"fas fa-user",
        "auth.Group":"fas fa-users",
        "admin.LogEntry":"fas fa-file",
        "mainapp.Department":"fa-solid fa-building-user",
        "mainapp.Events":"fa-light fa-calendar-circle-user",
        "mainapp.Leaves":"fas fa-door-open menu-icon",
        "mainapp.Notice":"fa-sharp fa-solid fa-bell",
        "mainapp.Payroll":"fas fa-money-check-dollar menu-icon",
        "mainapp.Salary": "fa-regular fa-money-bill-wave",
        "mainapp.Schedule": "fa-calendar-alt",
        "mainapp.Profile": "fa-solid fa-id-card",
        "mainapp.Attendance": "fa-solid fa-id-card",
        

        
    },
    
}