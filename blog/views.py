from django.shortcuts import render, redirect
from . models import Blog
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
# Create your views here.


def home(request):
    return render(request, 'base.html')


def hello(request):
    return render(request, 'about.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
     
        if username and firstname and lastname and password_1 and password_2 and email:
            if password_1==password_2:
                user = User(username=username,first_name=firstname, 
                last_name=lastname,email=email,password=password_2)
                user.save()
                return redirect('/')
            else:
                return redirect('/profile')
        else:
            return redirect('/profile')
    else:
        context={
            'user': User.objects.all()
        }
        return render(request, 'profile.html', context)
        
        # country = request.POST['country']
        

    #             form_save = User(username=username, firstname=firstname,
    #                                     lastname=lastname, password=password, email=email)
    #             form_save.save()
    #             return redirect('/')
    #     else:
    #         return redirect('/')
    # else:
    #     form_data = UserProfile.objects.all()
    #     return render(request, 'profile.html', {'form_data': form_data})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form_save.is_valid():
#             user = form_save.get_user()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        user= auth.authenticate( data=request.POST)
        return redirect('/blog_post')
    else:
        return render(request, 'login.html')
def blog_post(request):
    return render(request, 'blog_post.html')

