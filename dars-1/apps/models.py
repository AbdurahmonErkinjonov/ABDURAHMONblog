from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    page = models.IntegerField()
    price = models.IntegerField
    image = models.URLField()
    genre = models.ManyToManyField(Genre)
    description = models.TextField()
    def __str__(self):
        return f"{self.title} by {self.author}"
    