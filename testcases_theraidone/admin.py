from django.contrib import admin
from .models import Testcase

# Register your models here.

class TestcaseAdmin(admin.ModelAdmin):
	exclude = ('bunker_length')