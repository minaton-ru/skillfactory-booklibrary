from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name

class Friend(models.Model):  
    full_name = models.TextField()  
    email = models.EmailField()
    def __str__(self):
        return self.full_name

class Publisher(models.Model):  
    company = models.CharField(max_length=128)  
    def __str__(self):
        return self.company

class Book(models.Model):
    bookcover = models.ImageField(upload_to='images', blank=True)
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    friend = models.ForeignKey('Friend', on_delete=models.DO_NOTHING, null=True, blank=True) 
    authors = models.ManyToManyField(
        'Author',
        through='Inspiration',
        through_fields=('book', 'author'),
        related_name="inspired_authors"
    )
    def __str__(self):
	    return self.title

class Inspiration(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="inspired_works"
    )