from django.contrib import admin
from .models import Category, Blog, Full, Gallery

admin.site.register(Category)


class FullAdmin(admin.StackedInline):
    model = Full


class GalleryAdmin(admin.TabularInline):
    model = Gallery


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (FullAdmin, GalleryAdmin)
