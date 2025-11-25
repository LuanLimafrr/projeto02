from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'marca', 'preco', 'imagem', 'disponivel']
        # Aqui vamos estilizar os campos para ficarem bonitos com Bootstrap
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control'}),
            'disponivel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }