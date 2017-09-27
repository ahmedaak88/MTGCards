from django.shortcuts import render
from django.contrib.auth import authenticate , login ,logout
from .forms import UserSignUp ,UserLogin 
from django.shortcuts import render, redirect
from mainapp.models import Cards
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q






def list_of_cards(request):
    details = Cards.objects.all()
    query = request.GET.get("q")
    if query:
        details= details.filter(
            Q(name__icontains=query) | 
            Q(text__icontains=query) 
            ).distinct()
        paginator = Paginator(details, 10) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context = {
        "list" : contacts ,
        "user": request.user,
        }
    else:
        paginator = Paginator(details, 10) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        context = {
        "list" : contacts ,
        "user": request.user,
        }
    return render(request , 'listofcards.html' , context)



























#  the login and signup stuff 


def userlogin(request):
    context={}
    form = UserLogin()
    context['form'] = form 
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user= authenticate(username=username,password=password)
            if auth_user is not None:
                login(request,auth_user)
                return redirect("mainapp:home")

            messages.warning(request,"wrong user name or password")
            return redirect("mainapp:login")
        messages.warning(request,form.errors)
        return redirect("mainapp:login")
    return render(request, 'login.html',context)


def usersignup(request):
    context={}
    form = UserSignUp()
    context['form'] = form 
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            user.set_password(password)
            user.save()
            auth_user= authenticate(username=username,password=password)
            login(request,auth_user)
            return redirect("mainapp:home")
        messages.error(request,form.errors)
        return redirect("mainapp:signup")
    return render(request, 'signup.html',context)

def userlogout(request):
    logout(request)
    return redirect("mainapp:home")

def post_home(request):
   
    context = {
    "user": request.user,
    }
    return render(request, 'home.html', context)
