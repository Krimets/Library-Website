from django.urls import path
from authentication import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('', views.IndexView.as_view(), name='index'),
    path('users-search/', views.SearchView.as_view(), name='users-search'),

]
