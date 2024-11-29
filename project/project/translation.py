from modeltranslation.translator import TranslationOptions, register

from ..management.models import Property, Host


@register(Property)
class PropertyTranslation(TranslationOptions):
    fields = ["name", "description", "address", "city", "state"]


@register(Host)
class HostTranslation(TranslationOptions):
    fields = ["name", "surname"]
