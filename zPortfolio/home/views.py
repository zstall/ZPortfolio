from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from home.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template

# Create your views here.
class HomeView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        contact_name = form.cleaned_data['contact_name']
        contact_email = form.cleaned_data['contact_email']
        form_content = form.cleaned_data['form_content']

        template = get_template('contact_template.txt')
        context = {
            'contact_name': contact_name,
            'contact_email': contact_email,
            'form_content': form_content,
        }

        content = template.render(context)

        email = EmailMessage("New contact form submission", content, "zstall.com" + '', ['zstall4@gmail.com'], headers = {'Reply-To': contact_email })
        email.send()
        return super().form_valid(form)

class ThanksView(TemplateView):
    template_name = 'thanks.html'

class PcView(TemplateView):
    template_name = 'pc.html'

class AboutView(TemplateView):
    template_name = 'about.html'
