from django.shortcuts import render,redirect
from django.contrib import auth, messages # yes ma k message ho banera magako xam 
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        #register
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # checking if password match
        if password == password2:
            #check username is taken by other or not
            if User.objects.filter(username=username).exists():
                messages.error(request,'That Username is Taken')
                return redirect('register')
            else:
                # checking email, wheather it already exits or not
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email already taken by someone please choose another one')
                    return redirect('register')

                else:
                    # looks good
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    # yedi user lay register garesi logni garne banau na manh lagema
                    # auth.login(request,user)
                    # messages.success(request,'You are now Logged In')
                    # return redirect('index')
                    # if everything goes correct then it will take us on login panel after we have register 
                    user.save()
                    messages.success(request,"Thank you for register you account and can login now")
                    return redirect('login')
        else:
            messages.error(request,'Password do not Match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        #login
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now Logged in')
            return redirect('dashboard')

        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
        return
    else:
        return render(request,'accounts/login.html')

def logout(request):

    return redirect('index')

def dashboard(request):

    return render(request,'accounts/dashboard.html')