# encoding: utf-8

from customers.models import *

# Create your models here.

class Invoice(models.Model):
    STATES = (
	   ('a', 'active'),
	   ('c', 'closed'),
    )
    contractor = models.ForeignKey(Contractor)
    buyer = models.ForeignKey(Buyer)
    invoice_amount = models.DecimalField(max_digits=12, decimal_places=2)
    delay_days = models.PositiveIntegerField(max_length=3)
    create_date = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATES, default='a')

    def __unicode__(self):
        return u'Invoice ID#{}: {}, {}, {} руб., [{}]'.format(self.id, self.contractor, self.buyer, self.invoice_amount, self.create_date)



class Offer(models.Model):
    factor = models.ForeignKey(Factor)
    invoice = models.ForeignKey(Invoice)
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    interest_rate = models.DecimalField(max_digits=3, decimal_places=1)
    commission = models.DecimalField(max_digits=3, decimal_places=1)
    create_date = models.DateTimeField()
    change_date = models.DateTimeField()

    def __unicode__(self):
        return u'{}: {}'.format(self.factor, self.invoice)
