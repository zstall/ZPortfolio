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
        email.send_email()
        return super().form_valid(form)

class ThanksView(TemplateView):
    template_name = 'thanks.html'

class PcView(TemplateView):
    template_name = 'pc.html'

#
# def get_contact(request):
#     form_class = ContactForm
#
#     if request.method == 'POST':
#         form = form_class(data = request.POST)
#
#         if form.is_valid():
#             contact_name = request.POST.get('contact_name','')
#             contact_email = request.POST.get('contact_email','')
#             form_content = request.POST.get('content','')
#
#         template = get_template('contact_template.txt')
#
#         context = {
#             'contact_name': contact_name,
#             'contact_email': contact_email,
#             'form_content': form_content,
#         }
#
#         content = template.render(context)
#
#         email = EmailMessage("New contact form submission", content, "Your website" + '', ['zstall4@gmail.com'], headers = {'Reply-To': contact_email })
#         email.send()
#         return redirect('home')
#     return render(request, 'home.html', {'form', form_class})
