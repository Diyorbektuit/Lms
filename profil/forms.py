from django.forms import ModelForm
from Auth.models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm


class NameUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']


class PasswordUpdateForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['password1', 'password2']
