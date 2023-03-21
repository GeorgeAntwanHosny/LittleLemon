from django.shortcuts import render
from rest_framework import generics

from BookingAPI.models import Book
from BookingAPI.serializers import BookSerializer


# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer