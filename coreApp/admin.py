from django.contrib import admin
from .models import ContactMessage, HelpRequest

# Register your models here.

admin.site.register(ContactMessage)
admin.site.register(HelpRequest)

