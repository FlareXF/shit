from django import forms
from main.models import Sites

class SiteCommentCreate(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Sites
        fields = ['content']