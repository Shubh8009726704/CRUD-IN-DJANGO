from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')

        desc = data.get('desc')
        photo = request.FILES.get('file')
        
        Student.objects.create(pro_name=name,pro_price=price,pro_desc=desc,pro_photo=photo)       
        return redirect('read')
    return render(request,'create.html')

def read(request):
    data = Student.objects.all()
    #this is for search
    if request.GET.get('search'):
        data = data.filter(pro_name__icontains = request.GET.get('search'))
    return render(request,'read.html',{'data':data})

def delete(request,id):
    m = Student.objects.get(id=id)
    m.delete()
    return redirect('read')

def edit(request,id):
    query = Student.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = data.get('price')
        desc = data.get('desc')
        photo = request.FILES.get('file')
        
        query.pro_name =name
        query.pro_price = price
        query.pro_desc =desc
        if photo:
          query.pro_photo = photo
        query.save()        
        return redirect('read')
    return render(request,'update.html',{'x':query})

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
           messages.error(request,'Username already exists')           
           return redirect('register')
                  
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,            
                 )
        user.set_password(password)
        user.save()
        messages.success(request,'Account created Successfully')
        return redirect('register')
    return render(request,'register.html')

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username = username).exists():
              messages.error(request,'Invalid Username')           
              return redirect('login')
        user = authenticate(username = username,password = password)
        if user is None:
            messages.error(request,'Invalid Password')           
            return redirect('login')
        else:login(request,user)
        return redirect('create')
    return render(request,'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,'welcome.html')
    
