from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Student
from .forms import StudentForm
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cp = request.POST['cpassword']
        if password==cp:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL ALREADY REGISTERED')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email,
                                                password=password)
                user.save()
                # print('user created')
                messages.info(request, 'user created')
                return redirect('register')



        else:
            #print("PASSWORD NOT MATCHED")
            messages.info(request,"PASSWORD NOT MATCHED")
            return redirect('register')

    else:
        return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        messages.info(request,"EITHER USER NAME OR PASSWORD IS INCORRECT")
    return render(request,'signin.html')

def login(request):
    if request.method == 'POST':

      return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def addstudentData(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/account/viewstudentData")
            except:
                pass

    else:
        form = StudentForm()


    return render(request, 'addstudent.html',{'form':form})

def viewstudentData(request):
    form=Student.objects.all()
    return render(request, 'showstudent.html', {'form': form})

def viewstudentDelete(request,id):
    form = Student.objects.get(id=id)
    form.delete()
    return redirect("/account/viewstudentData")

def studentEdit(request,id):
    form = Student.objects.get(id=id)
    return render(request, 'editstudent.html', {'form': form})



def studentupdate(request,id):
    student= Student.objects.get(id=id)
    form=StudentForm(request.POST,instance=student)

    if form.is_valid():
        try:
            form.save()
            return redirect("/account/viewstudentData")
        except:
            pass




    else:
        print(form.errors)


    return render(request, 'editstudent.html',{'form':form})



