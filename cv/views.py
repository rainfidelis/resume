from django.http.response import BadHeaderError
from django.shortcuts import redirect, render
from .forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from config.settings import DEFAULT_FROM_EMAIL



def home(request):

    submitted = False
    form = ContactForm(request.POST)
    if request.method == "POST" and form.is_valid():
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

        # messages.add_message(request=request, message='Thanks! Your message was well received. Will reply shortly.', level=messages.SUCCESS)
        return redirect('/thank-you')

    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'submitted': submitted})


def thankyou(request):
    return render(request, 'thanks.html', {})