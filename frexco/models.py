from django.db import models

# Definindo classe região
class Region(models.Model):
    # Regiões que poderão ser cadastradas
    REGIONS = (
        ('Sul', 'S'),
        ('Centro-Oeste', 'CO'),
        ('Sudeste', 'SE'),
        ('Nordeste', 'NE'),
        ('Norte', 'N')
    )
    # Nome das regioes, restrigindo apenas às REGIONS definidas e criação de regiões duplidas também
    name = models.CharField(max_length=12, choices=REGIONS, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

# Definindo classe fruta
class Fruit(models.Model):
    name = models.CharField(max_length=50) # nome da fruta
    region = models.ForeignKey(Region, on_delete=models.CASCADE) # FK, se deletar região, deleta todas as frutas

    def __str__(self):
        return self.name