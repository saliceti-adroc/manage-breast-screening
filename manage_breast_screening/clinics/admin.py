from django.contrib import admin

from .models import Appointment, Clinic, ClinicSlot, Provider, ScreeningEpisode, Setting

admin.site.register(Appointment)
admin.site.register(Clinic)
admin.site.register(ClinicSlot)
admin.site.register(Provider)
admin.site.register(ScreeningEpisode)
admin.site.register(Setting)
