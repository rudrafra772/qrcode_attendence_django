from django.contrib import admin
from .models import Attendenc

# Register your models here.
@admin.register(Attendenc)
class AdminAttendenctModel(admin.ModelAdmin):
    list_display = ['id','name', 'date','entry_time','exit_time']