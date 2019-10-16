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
import logging


logger = logging.getLogger('users_log')
# Create your views here.
def welcome(request):
    try:
        return render(request, "users/welcome.html")
    except:
        logger.error("fail to render welcome page.")
        return HttpResponse({'message': 'fail to render welcome page.'}, status=500)
    
def welcomeUser(request):
    return render(request, "users/welcome_user.html")

def signup(request):
    try:
        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'You have signed up! Now sign in!')
                return redirect(signin)

        else:
            form = SignupForm()
        return render(request, "users/signup.html", {'form_signup': form})
    except:
        logger.error("fail to render signup page.")
        return HttpResponse({'message': 'fail to render signup page.'}, status=500)

def signin(request):
    try:
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
    except:
        logger.error("fail to render signin page.")
        return HttpResponse({'message': 'fail to render signin page.'}, status=500)

def signout(request):
    try:
        request.session.flush()
        Session.objects.all().delete()
        return render(request,"users/signout.html")
    except:
        logger.error("fail to render signout page.")
        return HttpResponse({'message': 'fail to render signout page.'}, status=500)

def admin1(request):
    try:
        users = User.objects.all()
        return render(request, "users/admin1.html", {'users': users})
    except:
        logger.error("fail to render admin.")
        return HttpResponse({'message': 'fail to render admin.'}, status=500)


def delete_user(request, pk):
    try:
        if request.method == "POST":
            User.objects.filter(id=pk).delete()
            users = User.objects.all()
            render(request, "users/admin1.html", {'users': users})
            return redirect(admin1)
        return redirect(admin1)
    except:
        logger.error("fail to delete user.")
        return HttpResponse({'message': f'fail to delete user, id={pk}.'}, status=500)

def update_user(request):
    try:
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
    except:
        logger.error("fail to update user.")
        return HttpResponse({'message': 'fail to update user.'}, status=500)


def create_user(request):
    try:
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
    except:
        logger.error("fail to create user.")
        return HttpResponse({'message': 'fail to create user.'}, status=500)




