from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class ArtesanoappConfig(AppConfig):
    name = 'artesanoapp'

class SuitConfig(DjangoSuitConfig):
    
    layout = 'horizontal'
    name = 'artesanoapp'