from django.shortcuts import render, redirect
from contact.forms import ContactForm


# -- Views - -
def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        context = {'form': form, 'site_title': 'Criar contato - '}
        if form.is_valid():
            form.save()
            return redirect('contact:create')
        else:
            form = ContactForm(request.POST)
            return render(request, 'contact/create.html', context)

    context = {'form': ContactForm(), 'site_title': 'Criar contato - ' }
    return render(request, 'contact/create.html', context)

