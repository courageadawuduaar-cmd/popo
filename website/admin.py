from django.contrib import admin
from .models import Service, Testimonial, Booking, Gallery
from .models import BeforeAfter
from .models import Barber


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "message")
    search_fields = ("name", "message")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "service", "date", "time", "phone")
    list_filter = ("service", "date")
    search_fields = ("name", "phone")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "created")


admin.site.register(BeforeAfter)


admin.site.register(Barber)

from django.contrib import admin

admin.site.site_header = ".popo.blades Administration"
admin.site.site_title = "PoPo Admin"
admin.site.index_title = "Welcome to .popo.blades Administration"