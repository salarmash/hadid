from django.contrib import admin
from .models import Team, Social


class SocialAdmin(admin.StackedInline):
    model = Social
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = (SocialAdmin,)
