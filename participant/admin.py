from django.contrib import admin
from team.models import Participant

# Register your models here.

class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',)
    list_filter = (
        'id',
        'firstName',
        'lastName',
        'mobileNo',
        'emailID',)

admin.site.register(Participant, ParticipantAdmin)
