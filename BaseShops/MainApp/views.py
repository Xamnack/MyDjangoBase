from django.shortcuts import render


def Main(request):
    return render(request, 'MainApp/Main.html')
