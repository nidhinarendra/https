from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello, world. You're in the https project.")
