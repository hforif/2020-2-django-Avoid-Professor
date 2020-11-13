from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm


# Create your views here.

def home(request):
    ctx = {}
    if request.user:
        ctx['user'] = request.user
    return render(request, 'core/home.html', ctx)


# example : owner와 status를 지정하는 예시
def example(request):
    ctx = {}
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.status = 'AC'
            item.owner = request.user
            item.save()
        return redirect('home')
    else:
        form = ItemForm()
        ctx['form'] = form
    return render(request, 'core/sample.html', ctx)
