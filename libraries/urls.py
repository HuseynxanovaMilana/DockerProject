from django.urls import path

from libraries.views import BooksAPI

urlpatterns = [
    path("api/", BooksAPI, name="books-api"),
]
