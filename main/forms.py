from django import forms
from main.models import Sites, SiteComment

class SiteCommentCreate(forms.ModelForm):
    content = forms.TextInput()

    class Meta:
        model = SiteComment
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content'].widget.attrs.update(placeholder='Написать комментарий...')