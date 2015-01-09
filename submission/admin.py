from django.contrib import admin
from submission.models import Submission

# Register your models here.

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'problem', 'stat', 'queries', 'cpu', 'memory')
    list_filter = ['user', 'problem', 'language',]
admin.site.register(Submission,SubmissionAdmin)
