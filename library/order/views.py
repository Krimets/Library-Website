

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView

from book.models import Book
from order.models import Order


class OrdersView(ListView):
    template_name = 'order/orders.html'

    def get_queryset(self):
        if self.request.user.role == 0:
            return Order.objects.filter(user=self.request.user)
        elif self.request.user.role == 1:
            return Order.objects.filter(end_at__isnull=True)


def orders_delete(request, id):
    record_order = Order.objects.get(pk=id)
    record_order.end_at = timezone.now()
    record_order.save()
    #record_order.delete()
    return HttpResponse("<script>alert ('Order is closed!'); window.location = '/orders';</script>")


def orders_create(request):
    if request.method == 'POST':
        book_id = request.POST.get('book')
        book = Book.objects.get(pk=book_id)
        plated_end_at = request.POST.get('plated_end_at')
        Order.create(user=request.user, book=book, plated_end_at=plated_end_at)

        return HttpResponse("<script>alert ('Order created!'); window.location = '/orders';</script>")

    return render(request, 'order/orders-create.html', {'books': Book.objects.all()})
