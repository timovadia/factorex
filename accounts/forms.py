# encoding: utf-8

from django import forms
from accounts.models import Invite
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _

class InviteCreationForm(forms.ModelForm):
    captcha = CaptchaField(label=_(u'Какие буквы на картинке ниже?'))
    class Meta:
        model = Invite
        widgets = {
          'email': forms.TextInput(attrs={'placeholder': 'Ваш адрес email'}),
          'contact_phone': forms.TextInput(attrs={'placeholder': '+7 900 555-44-33'})
        }
        fields = ('user_role', 'email', 'name', 'contact_phone', )