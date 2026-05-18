from django.shortcuts import render, redirect, get_object_or_404
import contact
from contact.forms import ContactForm
from django.urls import reverse
from contact.models import Contact


# -- Views - -
def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Criar contato - '
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)
        else:
            form = ContactForm(request.POST)
            return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'site_title': 'Criar contato - '
        }
    return render(request, 'contact/create.html', context)

# para atualização de dados é reaproveitado o formulario já criado,
# como o formulario é baseado
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
            'site_title': 'Criar contato - '
        }                                                    

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.pk)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'site_title': 'Criar contato - '
        }
    return render(request, 'contact/create.html', context)
