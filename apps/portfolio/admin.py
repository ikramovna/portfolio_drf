from django.contrib import admin

from apps.portfolio.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'keyword', 'image', 'url')


admin.site.register(Project, ProjectAdmin)
