from django.contrib import admin
from .models import Book, Hero

class HeroInLine(admin.StackedInline):
    model = Hero
    extra = 2


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']
    list_filter = ['title', 'pub_date']
    search_fields = ['tilte']
    list_per_page = 3
    inlines = [HeroInLine]

class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sex', 'content', 'book']
    list_filter = ['book']
    search_fields = ['name']
    list_per_page = 3

    #后台管理添加需要设置的信息
    #fields = ['book', 'name', 'content', 'gender']
    fieldsets = [('基础信息', {'fields': ['book', 'name']}),
                 ('详细信息', {'fields': ['content', 'gender']}), ]

#后台管理的配置文件
# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Hero)
