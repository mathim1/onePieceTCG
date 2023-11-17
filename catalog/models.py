from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.type


class Images(models.Model):
    image = models.TextField()

    def __str__(self):
        return self.image


class Idioma(models.Model):
    idioma = models.CharField(max_length=20)

    def __str__(self):
        return self.idioma


class Moneda(models.Model):
    moneda = models.CharField(max_length=20)

    def __str__(self):
        return self.moneda


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    descripcion = models.TextField()
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.TextField()
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre