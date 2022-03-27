from tabnanny import verbose
from django.apps import AppConfig


class AcmeCeoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Acme_Ceo'
    verbose_name = "Empresa Acme Ceo"
