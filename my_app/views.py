from django.shortcuts import render,redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from django.http import HttpResponse


from django.contrib.auth.models import User
from .forms import SignUpForm 

def index(request):
    return render (request ,"index.html")

def sign_in(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('user_name')
            first_name = form.cleaned_data.get('first_name') 
            last_name = form.cleaned_data.get('last_name') 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                my_user = User.objects.create_user(username=uname,first_name=first_name,last_name=last_name, email=email, password=password)
                my_user.save()
                return HttpResponse("Sign up successfully")
            except Exception as e:
                form.add_error(None, f"Error creating user: {e}")

    else:
        form = SignUpForm()

    return render(request, 'sign_in.html', {'form': form})


def login_view(request):  # Rename this function to avoid conflict
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's built-in authentication method
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return render (request ,"papa.html") 
        
             # Redirect to a homepage or dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


# @login_required
# def account_view(request):
#     return render(request, 'account.html')

# def back(request):
#     return render (request ,"papa.html")