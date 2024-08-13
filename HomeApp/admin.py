from django.contrib import admin
from .models import Hero, About, Service, ServiceItems, Testimonial, TestItems, Partner

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Partner)


class ServiceItemAdmin(admin.StackedInline):
    model = ServiceItems
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (ServiceItemAdmin,)


class TestItemAdmin(admin.StackedInline):
    model = TestItems
    extra = 1


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    inlines = (TestItemAdmin,)
