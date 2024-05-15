from django.forms import ModelForm
from .models import Group, Student


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop('request_user', None)
        super(GroupCreateForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(GroupCreateForm, self).save(commit=False)
        if self.request_user:
            instance.owner = self.request_user
        if commit:
            instance.save()
        return instance


class StudentCreateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class GroupEditForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']
