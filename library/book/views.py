from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from authentication.models import CustomUser
from book.models import Book
from order.models import Order


class BooksView(ListView):
    template_name = 'book/books.html'

    def get_queryset(self):
        return Book.objects.all()


class BooksSearchView(View):

    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search')
        try:
            result = Book.objects.get(name=search_value)
        except:
            try:
                result = Book.objects.get(author=search_value)
            except:
                try:
                    print('tttt')
                    result = Book.objects.get(description=search_value)
                except:
                    result = None
        return render(request, 'book/books-search.html', {'result': result})


class UserBooksSearchView(View):

    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search')
        try:
            user_result = CustomUser.objects.get(id=search_value)
        except CustomUser.DoesNotExist:
            return render(request, 'book/user-search.html', {'result': None})
        result = Order.objects.filter(user=user_result, end_at__isnull=True)
        result2 = []
        for _ in result:
            result2.append(_.book)
        return render(request, 'book/user-search.html', {'result': result2})

