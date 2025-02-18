from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book_categories'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    publication_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'