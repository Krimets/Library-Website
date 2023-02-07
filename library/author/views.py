from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from author.models import Author


class AuthorsView(ListView):
    template_name = 'author/authors.html'

    def get_queryset(self):
        if self.request.user.role == 0:
            return None
        else:
            return Author.objects.all()


def authors_delete(request, id):
    record = Author.objects.get(pk=id)
    if not record.books.all:
        return HttpResponse("<script>alert ('You cannot delete this author!'); window.location = '/authors';</script>")
    else:
        record.delete()
        return HttpResponse("<script>alert ('Author deleted!'); window.location = '/authors';</script>")



def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        Author.create(name=name, surname=surname, patronymic=patronymic)

        return HttpResponse("<script>alert ('Author created!'); window.location = '/authors';</script>")

    return render(request, 'author/create.html')
