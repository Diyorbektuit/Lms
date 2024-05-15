from django.forms import ModelForm
from Auth.models import CustomUser


class NameUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']