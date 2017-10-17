from django.http import HttpResponse


def ola(request):
    return HttpResponse("<h1>Guilherme<h1>")