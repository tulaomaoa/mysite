from django.db import models

# Create your models here.

#出版社

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)

    def __str__(self):
        return "<Publisher Object: {}>".format(self.name)


#图书

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, default='')
    def __str__(self):
        return "<Book Object: {}>".format(self.title)

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=16, null=False, unique=True)
    book = models.ManyToManyField(to='Book')

    def __str__(self):
        return "<Author Object: {}>".format(self.name)

