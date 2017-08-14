from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return "PUblisher " + self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    ISBN = models.CharField(max_length=20)
    summary = models.TextField()
    publisher = models.ForeignKey(Publisher)
    borrow_record = models.ManyToManyField('User', through='Borrow')
    
    def __str__(self):
        return "Book " + self.name + ": " + self.ISBN
    

class Section(models.Model):
    name = models.CharField(max_length=32)
    

class User(models.Model):
    django_user = models.OneToOneField(DjangoUser)
    role_choice = (
        (0, 'End User'),
        (1, 'Staff'),
        )
    role = models.IntegerField(choices=role_choice)
    

class Membership(models.Model):
    book = models.OneToOneField(Book)
    section = models.ForeignKey(Section)
    shelf = models.CharField(max_length=20)
    row = models.CharField(max_length=20)
    
    def adrs(self):
        return self.shelf + ', ' + self.row
    
class Borrow(models.Model):
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
