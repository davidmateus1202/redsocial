from django.shortcuts import render


def mi_vista(request):
    return render(request, 'sistemachat/index.html')