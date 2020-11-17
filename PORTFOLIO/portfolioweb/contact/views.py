from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            #redireccionamos
            email = EmailMessage(
                "Portfolio JMSB: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email,content),
                "no-contestar@inbox.mailtrap.io",
                ["josem.sb1993@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            #todo ha ido bien
                return redirect(reverse('contacto')+"?ok")
            except:
                #algo no ha ido bien
                return redirect(reverse('contacto')+"?fail")

    return render(request, "contact.html",{'form':contact_form})