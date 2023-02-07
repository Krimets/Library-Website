from django.urls import path
from author import views

urlpatterns = [
    path('', views.AuthorsView.as_view(), name='authors'),
    path('delete/<id>/', views.authors_delete, name='authors-delete'),
    path('create/', views.create, name='create'),
]
