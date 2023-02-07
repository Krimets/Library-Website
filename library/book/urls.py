from django.urls import path
from book import views

urlpatterns = [
    path('', views.BooksView.as_view(), name='books'),
    path('books-search/', views.BooksSearchView.as_view(), name='books-search'),
    path('user-search/', views.UserBooksSearchView.as_view(), name='user-search'),

]
