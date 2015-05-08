from django.contrib import admin

# Register your models here.
from .models import Account, GroupAccount

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'is_admin', 'date_joined')

admin.site.register(Account, AccountAdmin)
admin.site.register(GroupAccount)
