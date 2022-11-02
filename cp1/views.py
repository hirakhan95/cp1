from django.http import HttpResponse


def home(request):
    return HttpResponse("But I am only a home page go to <a href='/sky'>Sky</a>")