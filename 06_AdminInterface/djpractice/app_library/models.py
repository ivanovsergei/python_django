from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.id}. {self.name}, {self.country}, {self.city}'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    biography = models.TextField()
    personal_site = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'


class Book(models.Model):
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('r', 'Review'),
        ('p', 'Published'),
    ]
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_data = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
