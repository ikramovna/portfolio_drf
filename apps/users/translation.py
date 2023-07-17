from modeltranslation.translator import register, TranslationOptions

from apps.users.models import Project


@register(Project)
class ProjectTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'keyword')
