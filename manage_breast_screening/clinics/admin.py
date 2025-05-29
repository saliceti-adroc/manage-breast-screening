from django.contrib import admin

from .models import Appointment, Clinic, ClinicSlot, Provider, ScreeningEpisode, Setting


class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "clinic_slot__starts_at",
        "clinic_slot__duration_in_minutes",
        "status",
    ]

    @admin.display()
    def name(self, obj):
        return obj.screening_episode.participant.full_name


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Clinic)
admin.site.register(ClinicSlot)
admin.site.register(Provider)
admin.site.register(ScreeningEpisode)
admin.site.register(Setting)
