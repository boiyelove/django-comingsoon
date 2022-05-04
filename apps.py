from django.apps import AppConfig


class ComingsoonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comingsoon'

    def ready(self):
        import os
        from django.conf import settings
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        settings.STATICFILES_DIRS += (os.path.join(BASE_DIR, 'comingsoon/static/'),)
        from . import signals
