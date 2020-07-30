from django import forms 
from .validators import validate_url

class URLinputForm(forms.Form):
    url = forms.CharField(label='',validators=[validate_url],widget=forms.TextInput(attrs={"placeholder":"Long URL","class":"form-control"}))
    
    def clean(self):
        cleaned_data = super(URLinputForm, self).clean()
        url = cleaned_data.get('url')
        
    def clean_url(self):
        url = self.cleaned_data['url']
        return url