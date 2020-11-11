# encoding: utf-8
from django.contrib import admin

# Register your models here.
from exchange.models import Invoice, Offer

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ('invoice_amount', 'delay_days', 'create_date', 'status')
	
class OfferAdmin(admin.ModelAdmin):
   list_display = ('invoice', 'discount', 'interest_rate', 'commission', 'create_date')



admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Offer, OfferAdmin)

