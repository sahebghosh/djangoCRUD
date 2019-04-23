from django.db import models

class BookLibrary(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=100)

    def __str__(self):
        return self.name

