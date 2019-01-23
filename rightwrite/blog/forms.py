from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('user', 'title', 'language', 'text')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['user'].initial = self.request.user.username
        print(self.fields['user'].initial)

