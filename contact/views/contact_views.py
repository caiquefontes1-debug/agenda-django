from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {"contacts": contacts, 'site_title': 'Contatos - '}
    return render(
        request,
        'contact/index.html',
        context
    )


def search(request):
    # aprendendo a usar o get para pegar o valor do input de pesquisa, caso nao exista, retorna vazio
    # no django é possivel usar a variavel para filtrar o banco de dados
    # para usar AND, basta usar virgula, para usar OR, basta usar Q com pipe |
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    if search_value:
        contacts = Contact.objects\
        .filter(
            show=True
        )\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        )\
        .order_by('-id')

        context = {"contacts": contacts, 'site_title': 'Pesquisa - '}
        return render(
            request,
            'contact/index.html',
            context
        )


def contact(request, contact_id):
    # . get retorna um dicionario unico, ou seja, um unico contato
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {"contact": single_contact, 'site_title': site_title}
    
    return render(
        request,
        'contact/contact.html',
        context
    )

    
