from django.contrib import admin
from participant.models import Participant
# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'user',)
    list_filter = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'user',)

admin.site.register(Participant, ParticipantAdmin)
