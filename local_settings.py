import os

# Configuration de base de données par défaut pour le développement local
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bdd_bloc3_studi',
        'USER': 'yrae',
        'PASSWORD': 'Z1632522yde',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Configuration pour les tests
if 'TEST' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'bdd_bloc3_studi',
            'USER': 'yrae',
            'PASSWORD': 'Z1632522yde',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Configuration de debug
DEBUG = True

# Autres configurations spécifiques au développement local
ALLOWED_HOSTS = ['*']