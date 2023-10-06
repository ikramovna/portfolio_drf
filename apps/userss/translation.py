from modeltranslation.translator import register, TranslationOptions

from apps.userss.models import Project


@register(Project)
class ProjectTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'keyword')
