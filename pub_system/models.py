from django.db import models


class Publishing(models.Model):
    name = models.CharField("Название", max_length=256)
    address = models.CharField("Адрес", max_length=256)
    additional_info = models.TextField("Доп. информация")
    created = models.DateField("Дата основания")
    authors = models.ManyToManyField("Author", null=True)
    editors = models.ManyToManyField("Editor", null=True)
    active = models.BooleanField("Действующее", default=True)

    def __str__(self):
        return self.name + " (" + self.address + ")"


class Book(models.Model):
    name = models.CharField("Название", max_length=256)
    authors = models.ManyToManyField("Author")
    published_by = models.ForeignKey(Publishing, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.CharField("Жанр", max_length=128)
    published = models.DateField("Дата издания")
    isbn = models.CharField("ISBN в формате xxx-x-xxxx-xxxx-x", max_length=17)
    editor = models.ForeignKey("Editor", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Editor(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Sales(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    count_sales = models.IntegerField("Число проданных экземпляров")
    sale_price = models.IntegerField("Цена за проданный экземпляр")

    def __str__(self):
        return "Продана " + str(self.book) + "в количестве " + str(
            self.count_sales) + "по цене " + str(self.sale_price)
