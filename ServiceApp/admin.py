from django.contrib import admin
from .models import Service, Full, List, Process




class FullAdmin(admin.StackedInline):
    model = Full


class ListAdmin(admin.StackedInline):
    model = List
    extra = 3


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (FullAdmin, ListAdmin)

admin.site.register(Process)