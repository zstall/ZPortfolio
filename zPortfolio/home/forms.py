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


    contact_name = forms.CharField(label='', initial='Enter Name', required=True)
    contact_email = forms.EmailField(label='', initial='Enter Email', required=True)
    form_content = forms.CharField(
        label='',
        initial='How can I help?',
        required=True,
        widget=forms.Textarea
    )
