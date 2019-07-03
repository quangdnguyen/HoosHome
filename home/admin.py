from django.contrib import admin

# Register your models here.
from .models import Listing, Users

admin.site.register(Listing)
admin.site.register(Users)
