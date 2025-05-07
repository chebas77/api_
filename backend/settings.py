from django.contrib import admin
from .models import Tarea
from datetime import timedelta

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'completada', 'fecha_creacion')
    list_filter = ('completada',)
    search_fields = ('titulo', 'descripcion')

INSTALLED_APPS = [
    # ...existing apps...
    'drf_spectacular',
    'corsheaders',
]

MIDDLEWARE = [
    # ...existing middleware...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...existing middleware...
]

REST_FRAMEWORK = {
    # ...existing configuration...
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # Use drf-spectacular
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Only enable JSON responses
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Allow requests from the frontend
]
# Optionally, allow all origins (not recommended for production)










]    },        # ...existing configuration...        ],            BASE_DIR / 'templates',  # Add this line to include the templates directory        'DIRS': [        # ...existing configuration...    {TEMPLATES = [# CORS_ALLOW_ALL_ORIGINS = True