from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Proprietario(models.Model):
    nome = models.CharField(max_length=50,  null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=False)

    def __str__(self):
        return f'{self.nome} - {self.cpf}'


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.CharField(max_length=30)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT, related_name="veiculos")
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.modelo



class  Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)