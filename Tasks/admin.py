from django.contrib import admin
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'priorite', 'date_echeance', 'status')
    search_fields = ('titre', 'description')
    list_filter = ('status', 'priorite')

admin.site.register(Tasks)