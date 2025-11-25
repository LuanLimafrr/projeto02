from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

# --- ÁREA PÚBLICA (CLIENTE) ---
def home(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'loja/home.html', {'produtos': produtos})

# --- ÁREA DA GERÊNCIA (RESTRITA) ---
@login_required(login_url='/login/') # Só entra se estiver logado
def gerencia_dashboard(request):
    # Aqui o gerente vê todos os produtos, inclusive os indisponíveis
    produtos = Produto.objects.all()
    return render(request, 'gerencia/dashboard.html', {'produtos': produtos})

@login_required(login_url='/login/')
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gerencia_dashboard')
    else:
        form = ProdutoForm()
    
    return render(request, 'gerencia/form_produto.html', {'form': form})