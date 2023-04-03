from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'specialization', 'email', 'phone_number')
    list_filter = ('department',)
    search_fields = ('name', 'specialization')


admin.site.register(Doctor, DoctorAdmin)

