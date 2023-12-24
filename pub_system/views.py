from django.db.models import Count, Avg, Sum
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from pub_system.models import Book, Publishing, Author, Editor, Sales
from pub_system.serializers import (BookFullSerializer, AuthorIDSerializer, \
    PublishingSerializer, BookSerializer, SalesSerializer,
                                    EditorInfoSerializer, \
    EditorSerializer, AuthorSerializer)


# Create your views here.

class MainViewSet(GenericViewSet):

    @action(
        detail=False,
        methods=['GET'],
        serializer_class=BookFullSerializer,
        url_path="get_author_books/(?P<author_id>\w+)",
        url_name="get_author_books"
    )
    def get_author_books(self, request, author_id, *args, **kwargs):
        books = Book.objects.filter(authors=author_id)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'],
            serializer_class=PublishingSerializer)
    def get_active_publishing(self, request, *args, **kwargs):
        publishing = Publishing.objects.filter(active=True)
        serializer = self.get_serializer(publishing, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'],
            serializer_class=BookSerializer)
    def publish_book(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'],
            serializer_class=SalesSerializer)
    def make_sale(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'],
            serializer_class=EditorSerializer)
    def create_editor(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['GET'], serializer_class=AuthorSerializer)
    def get_author_with_different_publishing(self, request, *args, **kwargs):
        authors = Author.objects.annotate(
            num_publishers=Count('book__published_by', distinct=True)).filter(
            num_publishers__gt=1)
        serializer = self.get_serializer(authors, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['GET'],
        serializer_class=EditorSerializer,
        url_path="get_editors_worked_with_author/(?P<author_id>\w+)",
        url_name="get_editors_worked_with_author"
    )
    def get_editors_worked_with_author(self, request, author_id, *args,
                                       **kwargs):
        editors = Editor.objects.filter(book__authors=author_id)
        serializer = self.get_serializer(editors, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['GET'],
        serializer_class=BookFullSerializer,
        url_path="get_books_by_pub_and_editor/(?P<publishing_id>\w+)/("
                 "?P<editor_id>\w+)",
        url_name="get_books_by_pub_and_editor"
    )
    def get_books_by_pub_and_editor(
            self, request, publishing_id, editor_id, *args, **kwargs
    ):
        books = Book.objects.filter(editor_id=editor_id, published_by_id=publishing_id)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], serializer_class=BookFullSerializer)
    def get_bestsellers(self, request, *args, **kwargs):
        avg_sales = Sales.objects.aggregate(avg_sales=Avg("count_sales"))["avg_sales"]
        book_ids = list(Sales.objects.values("book_id").annotate(
            book_count_sales=Sum("count_sales")).filter(
            book_count_sales__gt=avg_sales).values_list("book_id", flat=True))
        books = Book.objects.filter(pk__in=book_ids)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], serializer_class=BookFullSerializer)
    def get_books_by_total_revenue(self, request, *args, **kwargs):
        books = Book.objects.annotate(total_revenue=Sum('sales__sale_price'))
        books = books.order_by('-total_revenue')
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
