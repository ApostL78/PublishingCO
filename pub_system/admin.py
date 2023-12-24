from django.contrib import admin

from pub_system.models import Book, Author, Editor, Publishing, Sales


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    list_display = ("name", "address")


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ("book", "count_sales", "sale_price")
