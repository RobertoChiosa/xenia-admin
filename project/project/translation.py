#  Copyright © Roberto Chiosa 2024.
#  Email: roberto@xeniapm.it
#  Last edited: 2/12/2024

# Third party imports
from modeltranslation.translator import TranslationOptions, register

from ..management.models import Host, Property


@register(Property)
class PropertyTranslation(TranslationOptions):
    fields = ["name", "description", "address", "city", "state"]


@register(Host)
class HostTranslation(TranslationOptions):
    fields = ["name", "surname"]
