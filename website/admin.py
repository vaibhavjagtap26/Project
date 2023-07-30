from django.contrib import admin
from website.models import enquiry_table
from website.models import booking_form

# Register your models here.
admin.site.register(enquiry_table)
admin.site.register(booking_form)
