from django.shortcuts import render


# Create your views here.

def home(request):
    ctx = {}
    if request.user:
        ctx['user'] = request.user
    return render(request, 'core/home.html', ctx)
