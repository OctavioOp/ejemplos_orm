from django.db import models
from django.db.models.base import Model

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    # agrega la hora y fecha actual de creacion de un objeto
    created_at = models.DateTimeField(auto_now_add=True)
    # agrega la ultima actualizacion del objeto
    updated_at = models.DateTimeField(auto_now=True)


class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(default='Dojo antiguo',max_length=255)

class Ninjas(models.Model):
    firs_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojos, related_name="ninjas",on_delete=models.CASCADE)



def __repr__(self) -> str:
    return f'{self.first_name} = {self.email_address}'
