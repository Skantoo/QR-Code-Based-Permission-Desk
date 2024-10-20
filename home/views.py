'''from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
#from datetime import datetime



from home.models import Admin
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def Home(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'home.html',context)
    #return HttpResponse("this is homepage ")

def Student(request):
    return render(request,'student.html')
    #return HttpResponse("this is Student page ")

"""def Admin(request):
    if request.method=="POST":
        Username = request.POST.get('Username')
        password = request.POST.get('password')
        print(Username, password)

        # check if user has entered correct credentials
        user = authenticate(Username=Username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'admin.html')

    return render(request, 'admin.html') """

    #if request.method == "POST":
    #      RNO = request.POST.get('RNO')
    #     SName = request.POST.get('SName')
    #      Reason = request.POST.get('Reason')
    #     admin = Admin(RNO=RNO, SName=SName, Reason=Reason)
     #     admin.save()
      #    messages.success(request, 'Your Request has been sent')
    #return render(request,'admin.html')
    #return HttpResponse("this is Admin page ")

def Faculty(request):
    return render(request,'faculty.html')
    #return HttpResponse("this is Faculty page ")

def Security(request):
    return render(request,'security.html')
    #return HttpResponse("this is Security-Personnel page ")
#for admin page
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/Admin")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')


    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")   

#for faculty page
def index1(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login1") 
    return render(request, 'index1.html')

def loginUser1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login1.html')


    return render(request, 'login1.html')

def logoutUser1(request):
    logout(request)
    return redirect("/")'''
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import Permissions
from django.contrib import messages

# Home view - No changes needed for now
def Home(request):
    context = {"variable": "this is sent"}
    return render(request, 'home.html', context)

# Student view - No changes needed for now
def Student(request):
    return render(request, 'student.html')

# Admin view
@login_required(login_url='/login')  # Requires authentication
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    if request.method == "POST":
        RNO = request.POST.get('RNO')
        SName = request.POST.get('SName')
        Reason = request.POST.get('Reason')
        admin = Admin(RNO=RNO, SName=SName, Reason=Reason)
        admin.save()
        messages.success(request, 'Your Request has been sent')
    return render(request, 'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/Admin")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/")

# Faculty view
@login_required(login_url='/login-faculty')  # Requires authentication for Faculty
def index1(request):
    return render(request, 'index1.html')

def loginUserFaculty(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/Faculty")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login-faculty.html')

def logoutUserFaculty(request):
    logout(request)
    return redirect("/")

#def manageperm(request):
    #return render(request,'manageperm.html')

# Security view
@login_required(login_url='/login-security')  # Requires authentication for Security
def index2(request):
    return render(request, 'index2.html')

def loginUserSecurity(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/Security")
        else:
            # No backend authenticated the credentials
            messages.error(request, 'Invalid login credentials')
    return render(request, 'login-security.html')

def logoutUserSecurity(request):
    logout(request)
    return redirect("/")
