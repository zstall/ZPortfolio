from django import forms
from home.models import Contact

class ContactForm(forms.Form):

    # class Meta():
    #     model = Contact
    #     fields = ('contact_name', 'contact_email', 'form_content')
    #
    # widgets = {
    #     'contact_name':forms.TextInput(attrs={'class':'textinputclass'}),
    #     'contact_email':forms.TextInput(attrs={'class':'textinputclass'}),
    #     'form_content':forms.TextInput(attrs={'class':'editable medium-editor-textarea postcontent'}),
    # }


    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    form_content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    
