from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, get_user
from django.contrib.auth.decorators import login_required
# Create your views here.

#This function will add new student info and show all students info
def add_show_data(request):
    currentuser = get_user(request)
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            # form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(name,email,password)
            register = StudentDetails(user=currentuser,name=name, email=email, password=password)
            register.save()
            return redirect("home")
    else:
        form = StudentRegistration()
    student = StudentDetails.objects.filter(user=currentuser.id)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'crud/index.html', context)

#This function is for update/edit a particular student info
@login_required
def update_info(request,id):
    if request.method == "POST":
        stud = StudentDetails.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=stud)
        if form.is_valid():
            form.save()
        return redirect("home")
    else:
        stud = StudentDetails.objects.get(pk=id)
        form = StudentRegistration(instance=stud)
    return render(request,"crud/update_student_data.html",{'form':form})

#This function will delete a particular student info
def delete_info(request, id):
    if request.method == "POST":
        stud = StudentDetails.objects.get(pk=id)
        stud.delete()
        return redirect("home")

def signup(request):
    if request.method == "GET":
        return render(request,"crud/signup.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('repassword')
        error_msg = None
        if password != re_password:
            error_msg = "Hey! Your Password Not Matched"
        elif User.objects.filter(username=username).first():
            error_msg = "This Username Has Been Already Registered"
        elif len(password) < 8:
            error_msg = "Password must Be 8 character"

        if not error_msg:
            user_object = User.objects.create(username=username)
            user_object.set_password(password)
            user_object.save()
            return redirect('home')
        else:
            data = {
                "error": error_msg,
            }
            return render(request, 'crud/signup.html', data)
def signin(request):
    if request.method == "GET":
        return render(request, 'crud/signin.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_object = User.objects.filter(username=username).first()
        error_msg = ""
        if user_object is None:
            error_msg = "User not found. Please try again"
        else:
            user = authenticate(username=username, password=password)
            if user is None:
                error_msg = "Wrong password."
            else:
                login(request, user)
                return redirect('home')
        print(username, password, user_object)

    return render(request, 'crud/signin.html', {'error': error_msg})
