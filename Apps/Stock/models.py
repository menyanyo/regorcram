from django.db import models


class Partners(models):
    name = models.CharfField(max_length=35)
    surnames = models.CharfField(max_length=35)
    email = models.CharfField(max_length=35)
    iban = models.CharfField(max_length=35)

    def __str__(self):
        return '{} {}'.format(self.name, self.surnames)


class Products(models):
    name = models.CharfField(max_length=35)
    stock = models.IntegerField()
    price = models.FloatField()
    image = models.ImageField(upload_to='PaintingImages/%Y/%m/%d')

    def __str__(self):
        return '{}, {}'.format(self.surname, self.name)


class Compositions(models):
    idproduct = models.ForeignKey(Products)
    idpainting = models.ForeignKey(Paintings)

    class Meta:
        unique_together = (('idproduct', 'idpainting'))


class Paintings(models):
    name = models.CharfField(max_length=35)
    creationdate = models.DateField()
    author = models.CharfField(max_length=35)


class Sales(models):
    idpartner = models.ForeignKey(Partners)
    idproduct = models.ForeignKey(Products)
    date = models.DateField()
