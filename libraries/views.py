from django.forms.models import model_to_dict
from django.http import JsonResponse

from libraries.models import BookModel


def BooksAPI(request):
    books = BookModel.objects.all()
    return JsonResponse(data=[model_to_dict(book) for book in books], safe=False)
