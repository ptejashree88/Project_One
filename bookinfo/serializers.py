from bookinfo.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['is_deleted']



class CustomSerializer(serializers.Serializer):
    a_model_serializer = AModelSerializer()
    b_model_serializer = serializers.ListField(child=CModelSerializer())
    another_field = serializers.CharField()

    def create(self, validated_data):
       print(validated_data)
       # Do your custom create

    def update(self, instance, validated_data):
       print(validated_data)
       # Do your custom update