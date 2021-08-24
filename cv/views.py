from django.http.response import BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from config.settings import DEFAULT_FROM_EMAIL



def home(request):

    submitted = False
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, DEFAULT_FROM_EMAIL, ['rainnyfidelis@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thank-you')

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'submitted': submitted})


def thankyou(request):
    return render(request, 'thanks.html', {})