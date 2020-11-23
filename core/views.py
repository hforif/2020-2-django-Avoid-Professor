from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemForm
from .models import Item, User

# Create your views here.
def home(request):
    items = Item.objects.all()
    ctx = {'items':items}
    if request.user:
        ctx['user'] = User.objects.order_by('-id')[0].name
    queryset = Item.objects.all()
    queryset.delete() #시작화면에 오면 아이템 초기화
    if User.objects.filter(del_assistance=True):
        user = User.objects.filter(del_assistance=True)
        for i in range(len(user)):
            user[i].del_assistance = False
            user[i].open_hydrant = False
            user[i].save()
    return render(request, 'core/home.html', ctx)

def search_window(request):
    ctx ={}
    return render(request, 'core/search_window.html', ctx)

def rank(request):
    ctx ={}
    return render(request, 'core/rank.html', ctx)


# example : owner와 status를 지정하는 예시
def example(request):
    ctx = {}
    if request.method == 'POST':
        print(request.POST)
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.status = 'AC'
            item.owner = request.user
            item.save()
        return redirect('home')
    else: #request.GET
        form = ItemForm()
        ctx['form'] = form
    return render(request, 'core/sample.html', ctx)

def door(request):
    items = Item.objects.all()
    ctx = {'items':items}
    if request.method == 'POST': #화분 클릭했을 때, 열쇠를 아이템모델에 넣어주는 작업
        if request.POST['Key'] == 'key':
            form = ItemForm()
            item = form.save(commit=False)
            item.name = '열쇠'
            item.bio = '무언가를 열 수 있는 키'
            item.status = 'AC'
            item.owner = User.objects.order_by('-id')[0]
            item.photo = 'key.jpg'
            item.save()
            return redirect('door')

        elif request.POST['Hydrant'] == 'hydrant':
            if not User.objects.filter(open_hydrant=True):
                users = User.objects.filter(open_hydrant=False) #정보확인 > 조교삭제
                for i in range(len(users)):
                    users[i].open_hydrant = True
                    users[i].save()
            return redirect('door')
    
    else:
        if User.objects.filter(del_assistance=True):
            print('success2')
            ctx['del_assistance'] = User.objects.filter(del_assistance=True)[0]
        if Item.objects.filter(name='열쇠'):
            print('success')
            ctx['key'] = Item.objects.get(name='열쇠')
        if User.objects.filter(open_hydrant=True):
            ctx['open_hydrant'] = True
        return render(request, 'core/door.html', ctx)

def record(request):
    ctx = {}
    return render(request, 'core/rank.html', ctx)

def lab(request):
    items = Item.objects.all()
    ctx = {'items':items}
    return render(request, 'core/lab.html', ctx)

def desk(request):
    items = Item.objects.all()
    ctx = {'items':items}
    if Item.objects.filter(name='열쇠'):
        ctx['key'] = Item.objects.get(name='열쇠')
    return render(request, 'core/desk.html', ctx)

def monitor(request):
    ctx = {}
    if request.method =='POST': 
        if request.POST['password'] == '12345678':
            if not User.objects.filter(del_assistance=True):
                user = User.objects.filter(del_assistance=False) #정보확인 > 조교삭제
                for i in range(len(user)):
                    print(user[i].del_assistance)
                    user[i].del_assistance = True
                    print(user[i].del_assistance)
                    user[i].save()
                return render(request, 'core/screen.html', ctx)
            else:
                return render(request, 'core/screen.html', ctx)
        else:
            return redirect('monitor')
    else:
        print(User.objects.filter(del_assistance=True))
        return render(request, 'core/monitor.html', ctx)


def drawer(request):
    items = Item.objects.all()
    ctx = {'items':items}
    if request.method == 'POST': #배열정보 획득
        print(request.POST)
        if request.POST['array_info'] == 'Array_info':
            form = ItemForm()
            item = form.save(commit=False)
            item.name = '구겨진 종이'
            item.bio = '이상한 내용들이 적혀있다.'
            item.status = 'AC'
            item.owner = User.objects.order_by('-id')[0]
            item.photo = '구겨진_종이.jpg'
            item.save()
            return redirect('drawer')
    else:
        if Item.objects.filter(name='구겨진 종이'):
            ctx['key'] = Item.objects.get(name='구겨진 종이')
        return render(request, 'core/drawer.html', ctx)

def ending(request):
    return render(request, 'core/ending.html')


################################################
def bookshelf(request) :
    items = Item.objects.all()
    ctx = {'items':items}
    return render(request, 'core/bookshelf.html', ctx)

def diary(request) :
    items = Item.objects.all()
    ctx = {'items':items}
    return render(request, 'core/diary.html', ctx)

def corner(request) :
    items = Item.objects.all()
    ctx = {'items':items}
    if request.method == 'POST' :
        if request.POST['post'] == 'trashcan' :
            form = ItemForm()
            item = form.save(commit=False)
            item.name = '교수님의 무지개색 양말'
            item.bio = '크크 이게 도움을 줄 거라고 생각하나?!'
            item.status = 'AC'
            item.owner = User.objects.order_by('-id')[0]
            item.photo = 'rainbowsocks.jpg'
            item.save()
            return redirect('corner')

        elif request.POST['post'] == 'hanger' :
            print(request.POST)
            form = ItemForm()
            item = form.save(commit=False)
            item.name = 'key2'
            item.bio = '서랍을 열 수 있는 열쇠'
            item.status = 'AC'
            item.owner = User.objects.order_by('-id')[0]
            item.photo = 'key2.jpg'
            item.save()
            return redirect('corner')
    else :
        if Item.objects.filter(name='교수님의 무지개색 양말') :
            ctx['socks'] = Item.objects.get(name='교수님의 무지개색 양말')
        if Item.objects.filter(name='key2'):
            ctx['key2'] = Item.objects.get(name='key2')
        return render(request, 'core/corner.html', ctx)
