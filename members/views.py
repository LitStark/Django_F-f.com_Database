from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from members.models import Member, UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def members(request):
    if request.user.is_authenticated:
        template = loader.get_template('all_members.html')
        allmembers = Member.objects.all().values()
        context = {
            'allmembers' : allmembers,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.error(request, "You are not logged in")
        return redirect('/login/')

def details(request, id):
    template = loader.get_template('details.html')
    member = Member.objects.get(id=id)
    context = {
        'member' : member,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    return render(request, 'main.html', {'user': request.user})

def testing(request):
    return render(request, 'testing.html')

def crm(request):
    template = loader.get_template('data_table.html')
    mydata=Member.objects.all()
    context = {
        'allmembers' : mydata,
    }
    return HttpResponse(template.render(context,request))

def add_member(request):
    template = loader.get_template('add_member.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    user=request.user
    fn=request.POST['first_name']
    ln=request.POST['last_name']
    em=request.POST['email']
    ph=request.POST['phone']
    ct=request.POST['city']
    st=request.POST['state']
    ad=Member(user=user,first_name=fn, last_name=ln, email=em, phone=ph, city=ct, state=st)
    ad.save()
    return HttpResponseRedirect(reverse('members'))

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return HttpResponseRedirect(reverse('members'))

def edit(request,id):
    template = loader.get_template('edit.html')
    member = Member.objects.get(id=id)
    context = {
        'member' : member,
    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    f=request.POST['first_name']
    l=request.POST['last_name']
    e=request.POST['email']
    p=request.POST['phone']
    c=request.POST['city']
    s=request.POST['state']
    mem=Member.objects.get(id=id)
    mem.first_name=f
    mem.last_name=l
    mem.email=e
    mem.phone=p
    mem.city=c
    mem.state=s
    mem.save()
    return HttpResponseRedirect(reverse('members'))

# Create Authentication System
# SignUp Page
def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render({},request))
# Handle SignUp
def handleSignup(request):
    if request.method != 'POST':
        return HttpResponseRedirect("404 - Page not found")
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['gender']
    email=request.POST['email']
    # username=request.POST['username']
    password=request.POST['pass1']
    confirmPassword=request.POST['pass2']
    
    if password != confirmPassword:
        messages.error(request, "Passwords do not match")
        return redirect('/signup/') 
    if User.objects.filter(email=email).exists():
        messages.error(request, "Email already exists")
        return redirect('/signup/')  
    if User.objects.filter(username=fname.lower()+'.'+lname.lower()).exists():
        messages.error(request, "Username already exists")
        return redirect('/signup/')
    if len(password) < 8:
        messages.error(request, "Password must be at least 8 characters long")
        return redirect('/signup/')
    if not any(char.isupper() for char in password):
        messages.error(request, "Password must contain at least one uppercase letter")
        return redirect('/signup/')
    if not any(char.islower() for char in password):
        messages.error(request, "Password must contain at least one lowercase letter")
        return redirect('/signup/')
    if not any(char.isdigit() for char in password):
        messages.error(request, "Password must contain at least one digit")
        return redirect('/signup/')
    if not any(char in '!@#$%^&*()_+' for char in password):
        messages.error(request, "Password must contain at least one special character")
        return redirect('/signup/')
    if len(fname) < 3 or len(lname) < 3:
        messages.error(request, "First name and last name must be at least 3 characters long")
        return redirect('/signup/')
    if fname.isalpha() == False or lname.isalpha() == False:
        messages.error(request, "First name and last name must contain only letters")
        return redirect('/signup/')
    
    else:
        create_user=User.objects.create_user(username=fname.lower()+'.'+lname.lower(),email=email,password=password) #
        create_user.first_name=fname
        create_user.last_name=lname
        create_user.save()
        
        add_on=UserProfile(user=create_user,dob=dob,gender=gender)
        add_on.save()
        
        messages.success(request, "Your account has been created successfully")
        return redirect('/login/')

# Login Page
def loginpage(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))
# Handle Login
def handleLogin(request):
    if request.method != 'POST':
        return HttpResponseRedirect("404 - Page not found")
    email= request.POST['login_email']
    password= request.POST['loginpass1']
    if not User.objects.filter(email=email).exists():
        messages.error(request,"Email does not exist")
        return redirect('/login/')
    username = User.objects.get(email=email).username
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        # messages.success(request,"You are logged in successfully")
        return render(request,'main.html')  
    else:
        messages.error(request,"Invalid credentials, please try again")
        return redirect('/login/')
    
    
def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"You are logged out successfully")
        return redirect('/login/')
    else:
        return redirect('404 - Page not found')
        
    