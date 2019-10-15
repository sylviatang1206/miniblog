from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .forms import SignupForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.http import HttpResponseNotFound
from django.contrib.sessions.models import Session
from django.contrib import messages



# Create your views here.
def welcome(request):
    return render(request, "users/welcome.html")
    
def welcomeUser(request):
    return render(request, "users/welcome_user.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have signed up! Now sign in!')
            return redirect(signin)

    else:
        form = SignupForm()
    return render(request, "users/signup.html", {'form_signup': form})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username,password=password, isadmin='0'):
            name = User.objects.filter(username=username,password=password).get()
            fullname = name.firstname + " " + name.lastname
            return render(request, 'users/welcome_user.html', {'name': fullname})
        elif User.objects.filter(username=username,password=password, isadmin='1'):
            return redirect(admin1)
        else:
            messages.error(request,"Invalid information, please try again.")
            return render(request,"users/signin.html")

    else:
        return render(request,"users/signin.html")

def signout(request):
    request.session.flush()
    Session.objects.all().delete()
    return render(request,"users/signout.html")

def admin1(request):
    users = User.objects.all()
    return render(request, "users/admin1.html", {'users': users})


def delete_user(request,pk):
    if request.method == "POST":
        User.objects.filter(id=pk).delete()
        users = User.objects.all()
        return render(request, "users/admin1.html", {'users': users})
    return HttpResponse("error")

def update_user(request):
    if request.method == "POST":
        id = request.POST['selectid']
        firstname = request.POST['input_fname']
        lastname = request.POST['input_lname']
        email = request.POST['input_email']
        website = request.POST['input_url']
        instance = User.objects.filter(id=id)
        instance.update(
            firstname=firstname, 
            lastname=lastname,
            email=email,
            website=website
        )
        users = User.objects.all()
        return render(request, "users/admin1.html", {'users': users})
    return HttpResponse("error")

def create_user(request):
    if request.method == "POST":
        username = request.POST['input_username']
        password = request.POST['input_password']
        firstname = request.POST['input_fname']
        lastname = request.POST['input_lname']
        email = request.POST['input_email']
        website = request.POST['input_url']
        instance = User.objects.create(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            website=website
        )
        users = User.objects.all()
        return render(request, "users/admin1.html", {'users': users})
    return HttpResponse("error")




