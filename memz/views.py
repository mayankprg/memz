from django.shortcuts import render



def front(request):
    context = { "hi": "hello"}
    return render(request, "index.html", context)