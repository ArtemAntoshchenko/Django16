from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_year=models.IntegerField()
    cost=models.DecimalField(max_digits=10, decimal_places=2)
    pages=models.IntegerField()
    genre = models.CharField(max_length=30, choices=[
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Science Fiction'),
        ('mystery', 'Mystery'),
        ('horror', 'Horror'),
        ('non-fiction', 'Non-Fiction'),
        ])
