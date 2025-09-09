from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(Ads)
class AdsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'info',)

@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Structure)
class StructureTranslationOptions(TranslationOptions):
    fields = ('name', 'info',)

@register(Director)
class DirectorTranslationOptions(TranslationOptions):
    fields = ('name', 'bio',)

@register(Readers)
class ReadersTranslationOptions(TranslationOptions):
    fields = ('text',)

@register(Catalog)
class CatalogTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

