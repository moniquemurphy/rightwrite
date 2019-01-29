from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ('title', 'language', 'text')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        self.user = self.request.user
        super(EntryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        form = super(EntryForm, self).save(commit=False)
        # save the user on it here
        form.user = self.user
        if commit:
            form.save()
        return form

