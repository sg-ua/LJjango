from django.shortcuts import render
from django.http import  HttpResponse
from .models import  Book

# Create your views here.
#编写第一个视图函数，http协议（基于请求-响应的一个协议，
def index(request):
    return HttpResponse("图书管理系统")

def detail(request, id):
    book = Book.objects.get(id=id)
    info = """
    书籍id： %s
    书籍名称： %s
    书籍发布日期： %s
    """ %(book.id, book.title, book.pub_date)
    return HttpResponse(info)