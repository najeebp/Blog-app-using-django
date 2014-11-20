from django.shortcuts import render
from blog3.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from forms import Login_form,Signup_form,forgot_password_form,password_change_form
from django.core.mail import send_mail
import base64




def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('user',False)
        password = request.POST.get('pass',False)
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(request.GET.get('next','/'))
                # name = User.objects.all()
                posts = Post.objects.all()
                print username
                # print posts
                return render(request, 'blog3/display2.html',{'posts':posts,'name':username})
            else:
                return HttpResponse("The password is valid, but the account has been disabled!")
        else:
            # return HttpResponse("The username and password were incorrect.")
            form = Login_form()
            error = 'username and password are incorrect'
            return render(request, 'blog3/Login_page.html',{'error':error,'form':form})

    else:
        form = Login_form()
        return render(request, 'blog3/Login_page.html',{'form':form})


def Signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        print username
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city = request.POST['city']
        user = User.objects.create_user(username, email, password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        print User.objects.all()
        form = Login_form()
        return render(request,'blog3/Login_page.html',{'form':form})
    else:
        form =Signup_form()
        return render(request, 'blog3/Signup_page.html',{'form':form})


def post_entry(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        tittle = request.POST.get('tittle')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        content = request.POST.get('content')
        date = request.POST.get('date')
        postt = Post(user=user,tittle=tittle,slug=slug,description=description,content=content,created=date)
        postt.save()
        posts = Post.objects.all()
        return render(request,'blog3/display2.html',{'posts':posts,'name':user})
    else:
        return render(request,'blog3/Posting_page.html')


@login_required(login_url='/login')
def home(request):
        posts = Post.objects.all()
        return render(request,'blog3/display.html',{'posts':posts})


def post_delete(request,post_id,name):
    print post_id
    deleting_entry = Post.objects.filter(id=post_id)
    deleting_entry.delete()
    posts = Post.objects.all()
    return render(request,'blog3/display2.html',{'posts':posts,'name':name})


def post_edit(request,post_id):
    print post_id
    edit_entry_del= Post.objects.get(id=post_id)
    edit_entry = Post.objects.get(id=post_id)
    edit_entry_del.delete()
    print edit_entry.tittle
    return render(request,'blog3/Editing_page.html',{'edit_entry':edit_entry})


def read_more(request,post_id):
    print post_id
    read_more_content = Post.objects.get(id=post_id)
    posts = Post.objects.all()
    return render(request,'blog3/read_more.html',{'read_more_content':read_more_content,'posts':posts})



def back_home(request):
    posts = Post.objects.all()
    return render(request,'blog3/display2.html',{'posts':posts})


def password_reset(request):
    if request.method =='POST':
        form = forgot_password_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            particular_person = User.objects.get(email=email)
            username = particular_person.username
            encrypt_string = base64.encodestring(username)
            print encrypt_string
            print username
            url = 'http://127.0.0.1:8000/changing-password/'+encrypt_string
            print url
            send_mail('password change', url, 'najeebp91@gmail.com',
            [email], fail_silently=False)
            print email
            return HttpResponse("Check your mail please")
    else:
        form = forgot_password_form()
        return render(request,'blog3/forgot_password.html',{'form':form})

def reset_password(request,encrypt_string):
    if request.method =='POST':
        form = password_change_form(request.POST)
        print form
        if form.is_valid():
            decrypt_string = base64.decodestring(encrypt_string)
            print decrypt_string
            after_getting_new_password = User.objects.get(username=decrypt_string)
            print after_getting_new_password
            password = form.cleaned_data['password']
            print password
            username = after_getting_new_password.username
            email = after_getting_new_password.email
            # username = form.cleaned_data['username']
            print username
            print email


           
            after_getting_new_password.set_password(password)
            after_getting_new_password.save()

            # email = form.cleaned_data['email']
            form = Login_form()
            return render(request,'blog3/Login_page.html',{'form':form})
        print form.errors


    else:
        form = password_change_form()
        encryptedstring = encrypt_string
        # decrypt_string = base64.decodestring(encrypt_string)
        return render(request,'blog3/password_reset.html',{'form':form,'encryptedstring':encryptedstring})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')