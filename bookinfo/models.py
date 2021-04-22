from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    qty = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_total_price(self):
        return self.qty * self.price    

    class Meta:
        db_table = "book"



def my_gen():
    yield 1
    yield 2
    yield 3
    yield 4


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
