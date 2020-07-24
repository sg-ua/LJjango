from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    def __repr__(self):
        return  '<Book: %s>' %(self.title)
    #字符串友好展示，在交互式环境测试时生效
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'books'
        verbose_name = '图书管理'
        verbose_name_plural = '图书管理'

class Hero(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=200)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    def __repr__(self):
        return  '<Hero: %s>' %(self.name)

    def sex(self):
        if self.gender:
            return "男"
        else:
            return "女"

    class Meta:
        db_table = 'heros'
        verbose_name = '人物管理'
        verbose_name_plural = '人物管理'