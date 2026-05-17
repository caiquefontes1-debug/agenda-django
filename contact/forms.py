from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

# -- Forms - -

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description','category'
                 )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'contact-create-form-input',
                    'placeholder': 'Digite o nome do contato'
                }
            ),
        }
    
    # Criar Validações Personalizadas
    def clean(self):
        # cleaned_data = self.cleaned_data
        cleaned_data = super().clean()
        # Acessar os dados do formulário usando cleaned_data.get('field_name')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        # Criar validação com os campos do formulário
        # No Exemplo abaixo, é verificado se o nome e sobrenome são iguais,
        # caso sejam, é criado uma mensagem de erro usando ValidationError
        if first_name == last_name:
            msg = ValidationError(
                'O nome e sobrenome não podem ser iguais',
                code='invalid'
            )
            # Caso a validação seja verdadeiro, é necessario adicionar
            # o error ao campo do formulário usando add_error
            # passando o nome do campo e a mensagem de erro
            self.add_error('first_name', msg) # type: ignore
            self.add_error('last_name', msg)
        
        # return super().clean()
        return cleaned_data