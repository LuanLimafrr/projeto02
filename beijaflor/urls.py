from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # <--- Importe isso
from loja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # --- Rotas de Autenticação ---
    # O Django já tem a lógica pronta, só precisamos dizer qual template usar
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # --- Rotas da Gerência ---
    path('gerencia/', views.gerencia_dashboard, name='gerencia_dashboard'),
    path('gerencia/novo/', views.cadastrar_produto, name='cadastrar_produto'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)