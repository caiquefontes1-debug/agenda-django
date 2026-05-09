from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from django import forms
from contact.models import Contact

# -- Forms - -
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'show',
                  'picture', 'category')    

# -- Views - -
def create(request):
    context = {
        'form': ContactForm(),
        'site_title': 'Criar contato - '
    }
    return render(
        request,
        'contact/create.html',
        context
    )

