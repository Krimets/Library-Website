from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from authentication.models import CustomUser


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        print(role)
        if role == 'Visitor':
            user = CustomUser.objects.create_user_guest(first_name=first_name, middle_name=middle_name,
                              last_name=last_name, email=email, password=password, role=0)
        else:
            user = CustomUser.objects.create_superuser(first_name=first_name, middle_name=middle_name, last_name=last_name,
                              email=email, password=password, role=1, is_staff=True, is_superuser=True)

        return HttpResponse("<script>alert ('You are registered!'); window.location = '/login';</script>")

    return render(request, 'authentication/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("<script>alert ('Login successful'); window.location = '/';</script>")
        else:
            return redirect('login')

    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    return HttpResponse("<script>alert ('You are logged out'); window.location = '/';</script>")


class IndexView(ListView):
    template_name = 'authentication/index.html'
    queryset = CustomUser.objects.all()


class UsersView(ListView):
    template_name = 'authentication/users.html'

    def get_queryset(self):
        if self.request.user.role == 0:
            return None
        else:
            return CustomUser.objects.all()


class SearchView(View):
    def get(self, request, *args, **kwargs):
        search_value = request.GET.get('search')
        if self.request.user.role == 0:
            result = None
        else:
            try:
                result = CustomUser.objects.get(email=search_value)
            except:
                result = None
        return render(request, 'authentication/users-search.html', {'result': result})


