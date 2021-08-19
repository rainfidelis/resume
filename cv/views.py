from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponseRedirect



def home(request):

    submitted = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            submitted = True
            return HttpResponseRedirect('/thank-you')

    else:
        form = ContactForm

    return render(request, 'index.html', {'form': form, 'submitted': submitted})


def thankyou(request):
    return render(request, 'thanks.html', {})