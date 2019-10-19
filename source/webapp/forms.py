from django import forms

from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
