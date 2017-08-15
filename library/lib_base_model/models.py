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
    
    def __str__(self):
        return "Section " + self.name

class User(models.Model):
    django_user = models.OneToOneField(DjangoUser)
    role_choice = (
        (0, 'End User'),
        (1, 'Staff'),
        )
    role = models.IntegerField(choices=role_choice)
    
    def __str__(self):
        return str(self.django_user)

class Membership(models.Model):
    book = models.OneToOneField(Book)
    section = models.ForeignKey(Section)
    shelf = models.CharField(max_length=20)
    row = models.CharField(max_length=20)
    
    def adrs(self):
        return self.shelf + ', ' + self.row

    def __str__(self):
        return str(self.book) + " is located at " + str(self.section) + " Shelf " + str(self.shelf) + " Row: " + str(self.row)
    
class Borrow(models.Model):
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)

    def __str__(self):
        return str(self.book) + " to " + str(self.user) + " at " + str(self.start) + " until " + str(self.end)

    def state(self):
        if start == None:
            return "Reserved"
        elif end == None:
            return "Taken"
        else:
            return "Brought Back"
