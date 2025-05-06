from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import HttpResponse

# Create your views here.
def register_view(request):
    print("Register View")
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request,user)
            #return HttpResponse('success')
            return redirect('dashboard')
    else:
        intail_data = {'username':'','Password1':'','Password2':''}
        form = UserCreationForm(intail_data)
    return render(request,'auth/register.html',{'form':form})
    
    
def login_view(request):
    if request.method =='POST':
        print("Login View")
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            print("Redirecting to dashboard")
            return redirect('dashboard')
    else:
        print("Login Else")
        intail_data = {'username':'','Password':''}
        form = AuthenticationForm(initial=intail_data)
    return render(request,'auth/login.html',{'form':form})

def dashboard(request):
    return render(request, 'auth/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')