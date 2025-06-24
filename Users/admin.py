from django.contrib import admin
from .models import Masters


class MastersAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)


admin.site.register(Masters)