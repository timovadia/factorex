from django.contrib import admin

# Register your models here.

from customers.models import Contractor, Factor, Buyer, FactorUser, ContractorUser

class ContractorAdmin(admin.ModelAdmin):
   list_display = ('name', 'inn', 'city', 'contact_phone', 'contact_email')

class FactorAdmin(admin.ModelAdmin):
   list_display = ('name', 'inn', 'city', 'contact_phone', 'contact_email')

class BuyerAdmin(admin.ModelAdmin):
   list_display = ('name', 'inn')


admin.site.register(Contractor, ContractorAdmin)
admin.site.register(Factor, FactorAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(FactorUser)
admin.site.register(ContractorUser)

