from django.shortcuts import render,redirect
from django.contrib import messages
from . models import shop
from . forms import ModeForm
from django.contrib.auth.models import User,auth
# Create your views here.
def demo(request):
    product=shop.objects.all()
    return render(request,'home.html',{'products':product})

def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect('login')
                print("user created")

        else:
            print("password not matched")
            return redirect('register')
        return redirect('login')
    else:
        return render(request,"register.html")



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')

    else:
        return render(request,"login.html")




# def detail(request,shop_id):
#
#     product=shop.objects.get(id=shop_id)
#
#
#     return render(request,'details.html',{'product':product})


def add_product(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        s=shop(name=name,desc=desc,img=img)
        s.save()
        print('add')
        return redirect('/')
    return render(request,'add_product.html')

def update(request,id):
    obj=shop.objects.get(id=id)
    form=ModeForm(request.POST or None,request.FILES or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj':obj,'form':form})

def delete(request,id):
    if request.method=='POST':
        obj=shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


