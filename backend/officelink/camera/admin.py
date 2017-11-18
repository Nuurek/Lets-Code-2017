from django.contrib import admin

from .models import Camera, Room, Measurement


admin.site.register(Camera)
admin.site.register(Room)
admin.site.register(Measurement)
