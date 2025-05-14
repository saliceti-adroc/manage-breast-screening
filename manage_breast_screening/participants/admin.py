from django.contrib import admin

from .models import Participant, ParticipantAddress


class AddressInline(admin.TabularInline):
    model = ParticipantAddress


class ParticipantAdmin(admin.ModelAdmin):
    inlines = [AddressInline]


admin.site.register(Participant, ParticipantAdmin)
