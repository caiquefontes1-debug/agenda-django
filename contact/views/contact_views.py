from django.shortcuts import render
from contact.models import Contact
from contact.


# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {"contacts": contacts}
    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request):
    sigle_contact = Contact