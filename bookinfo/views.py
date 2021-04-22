from django.shortcuts import render
from bookinfo.models import Book
from rest_framework.viewsets import ModelViewSet
from bookinfo.serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status


class BookViewSet(ModelViewSet):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        # print(request.data, type(request.data))
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    # 8000:book/b/get-book-price
    @action(methods=['get'], url_name="get-book-price",detail=True)
    def get_book_total_price(self, request, pk=None):
        book_obj = Book.objects.get(id=pk)
        ret_val = book_obj.get_total_price()  # float
        python_dict = {"Book Total Price": ret_val}
        return JsonResponse(python_dict)


from django.db import connection, transaction
def my_custom_sql():
    cursor = connection.cursor()

    # Data modifying operation - commit required
    cursor.execute("insert into bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    return row


