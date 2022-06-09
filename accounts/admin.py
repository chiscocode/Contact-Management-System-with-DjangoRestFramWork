from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email','contact_date')
  list_display_links = ('name','email')
  search_fields = ('name','email',)
  list_per_page = 25

class PickupAdmin(admin.ModelAdmin):
  list_display = ( 'uuid','sendername', 'recivername','senderemail','reciveremail','parcel','senderphone','reciverphone', 'request_date')
  list_display_links = ('uuid','sendername', 'recivername')
  search_fields = ('uuid','senderemail', 'reciveremail')
  list_per_page = 25

admin.site.register(Pickup, PickupAdmin)
admin.site.register(Contact, ContactAdmin)
