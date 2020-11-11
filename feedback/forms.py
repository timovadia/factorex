# encoding: utf-8

from django import forms
from feedback.models import Feedback
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _

class FeedbackForm(forms.ModelForm):
    captcha = CaptchaField(label=_(u'Какие буквы на картинке ниже?'))
    class Meta:
        model = Feedback
        widgets = {
          'message': forms.Textarea(attrs={'rows':5, 'cols':20, 'placeholder': 'Добрый день! ...'}),
          'email': forms.TextInput(attrs={'placeholder': 'example@gmail.com'}),
          'name': forms.TextInput(attrs={'placeholder': 'Фактор Факторов'}),
          'contact_phone': forms.TextInput(attrs={'placeholder': '+7 900 555-44-33'})
        }
        fields = ('email', 'contact_phone', 'name', 'message',)