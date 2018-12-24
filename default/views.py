from django.shortcuts import render, redirect


from default.models import User
from default.models import LinkMan
from default.forms import LinkM
from django.db.models import Q


# Create your views here.
def index(request):
    return redirect('/login/')


def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        message = "登录信息不完整！"
        if name and pwd:
            try:
                user = User.objects.get(name=name)
                if user.password == pwd:
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/linkBook/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/login/')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        message = "注册信息不完整！"
        if name and pwd1 and pwd2:
            if pwd1 == pwd2:  # 判断两次密码是否一致
                same_user = User.objects.filter(name=name)
                if same_user:
                    message = "用户名已存在！"
                else:
                    new_user = User()
                    new_user.name = name
                    new_user.password = pwd1
                    new_user.save()
                    return redirect('/login/')
            else:
                message = "两次密码不一致！"
        return render(request, 'register.html', {'message': message})
    return render(request, 'register.html')


def link_book(request):
    user_id = request.session['user_id']
    linkman = LinkMan.objects.filter(user=user_id)
    return render(request, 'linkBook.html', {'linkMan': linkman})


def add(request):
    if request.method == 'POST':
        form_link = LinkM(request.POST)
        if form_link.is_valid():
            user_id = request.session['user_id']
            user = User.objects.get(id=user_id)
            linkman = LinkMan(
                user=user,  # 这个地方得用user对象，不能直接用user_id
                name=form_link.cleaned_data['name'],
                mail=form_link.cleaned_data['mail'],
                img=form_link.cleaned_data['img'],
                phoneNumber=form_link.cleaned_data['phoneNumber'],
                address=form_link.cleaned_data['address'],
                qq=form_link.cleaned_data['qq'],
            )
            linkman.save()
            return redirect('/linkBook/')
    else:
        form_link = LinkM()
    return render(request, 'addMan.html', {'form': form_link})


def update(request):
    if request.method == 'GET':
        lmid = request.GET['lmid']
        linkman = LinkMan.objects.get(id=lmid)
        return render(request, 'update.html', {'linkman': linkman})
    elif request.method == 'POST':
        lmid = request.POST['lmid']
        linkman = LinkMan.objects.get(id=lmid)
        linkman.name = request.POST['name']
        linkman.phoneNumber = request.POST['phoneNumber']
        linkman.mail = request.POST['mail']
        linkman.address = request.POST['address']
        linkman.qq = request.POST['qq']
        linkman.save()
        return redirect("/linkBook/")


def dele(request):
    lmid = request.GET['lmid']
    LinkMan.objects.get(id=lmid).delete()
    return redirect("/linkBook/")


def search(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyWord')
        linkman = LinkMan.objects.filter(
            Q(user__exact=request.session['user_id']) &
            (Q(name__icontains=keyword) |
            Q(phoneNumber__icontains=keyword) |
            Q(mail__icontains=keyword) |
            Q(address__icontains=keyword) |
            Q(qq__icontains=keyword))
        )
        if linkman:
            return render(request, 'search.html', {'linkMan': linkman})
        else:
            error_msg = '没找到符合条件的结果！提示：不支持中文检索'
            return render(request, 'search.html', {'error_msg': error_msg})
    return render(request, 'search.html')
