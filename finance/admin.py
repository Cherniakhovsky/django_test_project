from django.contrib import admin
from finance.models import Client, Cost
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ('username','passport_number')

class CostAdmin(admin.ModelAdmin):
    list_display = ('username','date', 'cost_description', 'cost', 'balance')


admin.site.register(Client,ClientAdmin)
admin.site.register (Cost,CostAdmin)