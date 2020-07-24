from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    def __repr__(self):
        return  '<Book: %s>' %(self.title)
    class Meta:
        db_table = 'books'

class Hero(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=200)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    def __repr__(self):
        return  '<Hero: %s>' %(self.name)
    class Meta:
        db_table = 'heros'