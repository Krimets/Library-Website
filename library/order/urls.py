from django.urls import path
from order import views

urlpatterns = [
    path('', views.OrdersView.as_view(), name='orders'),
    path('delete/<id>/', views.orders_delete, name='orders-delete'),
    path('orders-create/', views.orders_create, name='orders-create'),
]
