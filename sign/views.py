from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

# 登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'super' and password == '123':
            return HttpResponse('login success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})