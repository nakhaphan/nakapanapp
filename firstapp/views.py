from django.shortcuts import render
from django.template import loader
from firstapp.models import Person
# from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user
from django.shortcuts import render, redirect

# Create your views here.

def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'KnM092PGWugC9vjLa89IJkHP1vGAtDTCe0G5ERQvMUo'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers ,data=payload,files=file)

def index(request):
    c_user =''
    if request.user.is_authenticated:
        c_user = request.user.username
    return render(request,'index.html',{"user_name":c_user})

def zero(request):
    return render(request,'zero.html')

def testparasmeter(request):
    message = "Test parameter"
    dictest = {
        'para1':'zero1',
        'para2':'zero2',
        'para3':'zero3',
    }
    return render(request,'parameter.html',{"message":message,"dictest1":dictest})    

def getdata(request):
    userdata = User.objects.all()
    #reportget =  Person.objects.get(user_name="nakapan2")
    #reportfilter = Person.objects.filter(user_name="nakapan")
    return render(request,'getdata.html',{'userdata':userdata})

def testform(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        Locate = request.POST.get('Locate')
        print("user name :" +user_name)
        print("Locate :" + Locate)
        addperson = Person(user_name=user_name,Locate=Locate)
        addperson.save()

    return render(request,'testform.html')

def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        user = User.objects.create_user(user_name,'nakapan@hotmail.com',pass_word,first_name='peane3',last_name='peakorat')
        user.save()

    return render(request,'sign_up.html')

def log_in(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pass_word = request.POST.get('pass_word')
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            login(request,user)
            message = "Hi Team User: {} Login Complete".format(user)
            lineNotify(message)
            return redirect(index) 
    return render(request,'log_in.html',{'erroruser':'Error BAD Username Or Password'})

def sign_out(request):
    logout(request)
    return redirect(index) 

def secrete1(request):
    if request.user.is_authenticated:
        c_user = request.user.username
        return render(request,'secrete1.html',{"user_name":c_user})
    return redirect(log_in)         

def secrete2(request):
    if request.user.is_authenticated:
        c_user = request.user.username
        return render(request,'secrete2.html',{"user_name":c_user})
    return redirect(log_in) 
