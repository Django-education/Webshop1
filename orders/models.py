from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
from goods.models import Product
=======
from goods.models import Product
from django.contrib.auth.models import User
>>>>>>> 9800cbb47d5bb33a0326cecb50d2a383689eee45
from django.utils import timezone


class Order2(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
=======

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
>>>>>>> 9800cbb47d5bb33a0326cecb50d2a383689eee45
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.title)
