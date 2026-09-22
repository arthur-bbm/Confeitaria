from django.db import models

class Bolo(models.Model):
    nome = models.CharField(max_length=255)
    sabor = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='fotos_bolo', blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
