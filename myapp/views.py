from django import forms
from django.forms.models import fields_for_model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CompanyForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#for models
from .models import Company


# Create your views here.
def mainPage(request):
    companies=Company.objects.all()[:4].all()
    context={'companies':companies}
    return render(request, 'main/index.html',context)

def discoverPage(request):
    company=Company.objects.all()
    count=company.count()
    search=request.GET.get('search')
    if search and search!='':
        result=Company.objects.filter(company_name=search).all()
        
        print(result)
    else:
        result=None
    latest=Company.objects.filter().order_by('-company_added')[0:4]     
    context={'count':count, 'result':result, 'latest':latest}
    return render(request, "main/discover.html", context)    


#profile page here
def accountPage(request):
    users=Company.objects.all()
    context={'users':users}    
    return render(request, 'main/profile.html',context)

def ViewAccountPage(request,pk):
    company=Company.objects.get(id=pk)
    context={'company':company}
    return render(request, 'main/viewAccount.html',context)


def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            #user=form.cleaned_data.get('username')
            #messages.success(request, 'Account was created for '+ user)
            return redirect('loginPage')

    context={'form':form}
    return render(request, 'main/register.html', context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Password or username is incorrect!')
            return render(request, 'main/login.html')     
    context={}
    return render(request, 'main/login.html',context)


def logoutPage(request):
    logout(request)
    return redirect('mainPage')      


def userRegisterPage(request):
    form=CompanyForm()    
    if request.method=='POST':
        form=CompanyForm(request.POST, request.FILES)
        if form.is_valid():
             company_form=form.save(commit=False)
             company_form.owner=request.user
             print(company_form)
             company_form.save()
             return redirect('/')    

    context={'form':form}
    return render(request, 'main/accountss.html', context)    

def editPage(reuqest):
    pass