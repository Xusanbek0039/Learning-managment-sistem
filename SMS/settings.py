"""
Django loyihasi uchun sozlamalar fayli (settings.py)

Bu fayl 'django-admin startproject' yordamida avtomatik yaratilgan.

Batafsil: https://docs.djangoproject.com/en/2.2/topics/settings/
"""

import os
import posixpath
import environ

# Muhit o'zgaruvchilarini o'qish (env fayldan)
env = environ.Env()

# Loyihani asosiy katalogi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Xavfsizlik: maxfiy kalit (productionda maxfiy saqlang!)
SECRET_KEY = "o!ld8nrt4vc*h1zoey*wj48x*q0#ss12h=+zh)kk^6b3aygg=!"

# Ishlab chiqish uchun True, serverda esa False bo'lishi kerak
DEBUG = True

# Ruxsat etilgan domenlar
ALLOWED_HOSTS = ["*"]  # serverda domen nomini aniq yozing

# Maxsus foydalanuvchi modeli
AUTH_USER_MODEL = "accounts.User"

# Django asosiy ilovalari
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# settings.py

SESSION_COOKIE_AGE = 3 * 60 * 60  # 3 soat (sekundlarda)
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Uchinchi tomon ilovalari (3rd-party)
THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
    "rest_framework",
]

# Crispy Forms sozlamalari (Bootstrap 5 uchun)
CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap5"]
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Loyihadagi o'zimiz yozgan ilovalar
PROJECT_APPS = [
    "app.apps.AppConfig",
    "accounts.apps.AccountsConfig",
    "course.apps.CourseConfig",
    "result.apps.ResultConfig",
    "search.apps.SearchConfig",
    "quiz.apps.QuizConfig",
    "payments.apps.PaymentsConfig",
]

# Umumiy barcha ilovalar ro‘yxati
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# Middlewarelar (sahifalar orasidagi ishlovchilar)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL konfiguratsiyasi
ROOT_URLCONF = "SMS.urls"

# Shablonlar (template) sozlamalari
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI va ASGI sozlamalari
WSGI_APPLICATION = "SMS.wsgi.application"
ASGI_APPLICATION = "SMS.asgi.application"

# Ma'lumotlar bazasi sozlamalari (hozircha sqlite3)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# PostgreSQL ishlatmoqchi bo‘lsangiz quyidagilarni faollashtiring:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": env("DB_NAME"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     }
# }

# Model yaratishda avtomatik ID maydoni
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Parol validatsiyalari
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Til va vaqt konfiguratsiyasi
LANGUAGE_CODE = "uz-UZ"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Statik fayllar (CSS, JS va h.k.)
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ["staticfiles"]))

# Media fayllar (yuklangan fayllar)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Email orqali xabar yuborish sozlamalari (hozircha to‘ldirilmagan)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ""  # Gmail manzilingiz
EMAIL_HOST_PASSWORD = ""  # Gmail parolingiz yoki app parol

# Tizimga kirgandan keyin yo‘naltiriladigan sahifa
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# DRF (Django REST Framework) sozlamalari
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
}

# Stripe to‘lov tizimi uchun maxfiy kalitlar (test uchun)
STRIPE_SECRET_KEY = "d42svs4dv"
STRIPE_PUBLISHABLE_KEY = "sdvsdv54"
