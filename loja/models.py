from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço (R$)")
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name="Foto")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível no Site?")

    def __str__(self):
        return f"{self.nome} ({self.marca})"