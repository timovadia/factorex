# encoding: utf-8

from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.edit import CreateView
from accounts.forms import InviteCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import Invite
from mail.utils import *
from django.conf import settings

# Create your views here.

class InviteCreate(CreateView):
    form_class = InviteCreationForm
    template_name = 'invite_new.html'
    success_url = 'success'

@receiver(post_save, sender=Invite)
def invite_save(instance, created, **kwargs):
    if created:
        send_mail(
            to_emails=[instance.email],
            from_email=settings.DEFAULT_FROM_EMAIL,
            subject=('Ваша заявка успешно принята! factorex.ru')
        )

def invite_success(request):
        return render(request, 'invite_success.html')