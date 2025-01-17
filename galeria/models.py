from datetime import datetime
from django.db import models

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    data_fotografia = models.DateTimeField(default=datetime.now , blank=False)
    publicada = models.BooleanField(default=False)
 

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"