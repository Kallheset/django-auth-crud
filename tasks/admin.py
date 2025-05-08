from django.contrib import admin
from .models import task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'datecompleted', 'important', 'user')
    search_fields = ('title', 'description')

admin.site.register(task, TaskAdmin)