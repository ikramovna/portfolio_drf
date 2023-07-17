from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.users.models import Project


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    pass
