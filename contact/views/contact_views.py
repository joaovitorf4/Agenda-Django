from contextlib import ContextDecorator

from contact.models import Contact
from django.shortcuts import render


def index(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(
        request, 
        'contact/index.html',
        context,
    )
