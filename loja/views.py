from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# --- FUNÇÃO DE SEGURANÇA (O GUARDA-COSTAS) ---
def checar_se_eh_equipe(user):
    # Retorna True se o usuário for "Staff" (Equipe/Admin)
    return user.is_staff

# --- ÁREA PÚBLICA (Qualquer um acessa) ---

def home(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'loja/home.html', {'produtos': produtos})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Vai para o login após criar conta
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/cadastro.html', {'form': form})

# --- ÁREA RESTRITA (Só Equipe acessa) ---

@login_required
@user_passes_test(checar_se_eh_equipe) # <--- Só passa se for da equipe
def gerencia_dashboard(request):
    produtos = Produto.objects.all()
    return render(request, 'gerencia/dashboard.html', {'produtos': produtos})

@login_required
@user_passes_test(checar_se_eh_equipe) # <--- Só passa se for da equipe
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gerencia_dashboard')
    else:
        form = ProdutoForm()
    
    return render(request, 'gerencia/form_produto.html', {'form': form})