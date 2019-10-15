from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .forms import SignupForm
from django.shortcuts import redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.http import HttpResponseNotFound






# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # data = request.POST.copy()
            # firstname = data.get('firstname')
            # lastname = data.get('lastname')
            # return render(request, 'users/welcome_user.html', {"firstname": firstname, "lastname": lastname})
            # firstname = form.cleaned_data['firstname']
            # request.session['firstname'] = firstname
            # return render(request, 'welcome_user.html', {"firstname" : firstname})
            return redirect(signin)

    else:
        form = SignupForm()
    return render(request, "users/signup.html", {'form_signup': form})
def check(request):
    print("check something", request.POST['username'])

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
            return render(request,"users/signin.html")

    else:
        return render(request,"users/signin.html")
def signout(request):
    request.session.flush()
    return render(request,"users/signout.html")
def admin1(request):
    users = User.objects.all()
    return render(request, "users/admin1.html", {'users': users})
def welcomeUser(request):
    return render(request, "users/welcome_user.html")
def welcome(request):
    return render(request, "users/welcome.html")


def get_users(request):
    if request.method == "GET":
        #users = list(User.objects.values())
        users = {'name': 'jj'}
        print(users)
        return JsonResponse(users, safe=False)
    else:
        return HttpResponseNotFound("This method doesn't exist.")
def update_user(request):
    if request.method == "PUT":
        pass

    pass
def delete_user(request):
    pass
    if request.method == "DELETE":
        User.objects.filter(id=userid).delete()

    pass


