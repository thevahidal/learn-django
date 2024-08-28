from rest_framework import serializers


class BooksSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    pages = serializers.IntegerField()
