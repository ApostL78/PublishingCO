from rest_framework import serializers

from pub_system.models import Publishing, Author, Book, Editor, Sales


class PublishingNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publishing
        fields = ["name"]


class AuthorIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["pk"]


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"


class AuthorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        exclude = ["id"]


class EditorInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editor
        exclude = ["id"]


class EditorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Editor
        fields = "__all__"


class BookFullSerializer(serializers.ModelSerializer):
    published_by = PublishingNameSerializer()
    editor = EditorInfoSerializer()
    authors = AuthorInfoSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"


class PublishingSerializer(serializers.ModelSerializer):
    editors = EditorInfoSerializer(many=True)
    authors = AuthorInfoSerializer(many=True)

    class Meta:
        model = Publishing
        fields = "__all__"


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = "__all__"
