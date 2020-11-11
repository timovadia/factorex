from django import forms
from accounts.models import FexUser



class RegistrationForm(forms.Form):
    TYPE_CHOICES = (
        ('f', u'Factor (investor)'),
        ('c', u'Contractor (provider)'),
    )

    user_role = forms.ChoiceField(choices=TYPE_CHOICES, label=u'User role')
    email = forms.EmailField(label=u'Email', max_length=80)
    password1 = forms.CharField(label=u'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label=u'Password (Again)', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError('Required field')
        if FexUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken.')
        return email