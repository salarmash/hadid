from django.contrib import admin
from .models import Category, Project, Full, Detail, Gallery, Gallery2

admin.site.register(Category)


class FullAdmin(admin.StackedInline):
    model = Full


class DetailAdmin(admin.StackedInline):
    model = Detail


class GalleryAdmin(admin.TabularInline):
    model = Gallery


class Gallery2Admin(admin.TabularInline):
    model = Gallery2


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (DetailAdmin, GalleryAdmin, Gallery2Admin, FullAdmin)
