from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from home.forms import ContactForm

# Create your views here.
class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def from_valid(self, form):
        form.send_email()
        return super().form_valid(form)
