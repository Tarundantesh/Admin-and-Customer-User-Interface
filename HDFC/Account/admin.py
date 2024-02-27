from django.contrib import admin
from Account.models import AccountHolder
# Register your models here.
class Manager(admin.ModelAdmin):
    list_display=['Name','Aadhar','PAN','Contact','Balance','Account_Type']
admin.site.register(AccountHolder,Manager)
