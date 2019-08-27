from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
User = get_user_model()


def login(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                next_url = request.POST.get('next')
                return redirect(next_url, 'home')
            else:
                return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'},
                              {'Forgot': 'Forgot Your Password?'})
        else:
            return render(request, 'accounts/login.html', {'error': 'All fields are required'})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['usernames'].isspace()
        password = request.POST['passwords'].isspace()
        password1 = request.POST['passwords1'].isspace()
        email = request.POST['email'].isspace()
        first_name = request.POST['first_name'].isspace()
        last_name = request.POST['last_name'].isspace()
        if not (username or password or password1 or email or first_name or last_name):
            if request.POST['passwords'] == request.POST['passwords1']:
                if len(request.POST['passwords']) >= 8:
                    try:
                        User.objects.get(username=request.POST['usernames']) or User.objects.get(email=request.POST['email'])
                        return render(request, 'accounts/signup.html', {'error': 'Username or Email already associated with an account'})
                    except User.DoesNotExist:
                        user = User.objects.create_user(request.POST['usernames'], password=request.POST['passwords'])
                        user.email = request.POST['email']
                        user.first_name = request.POST['first_name']
                        user.last_name = request.POST['last_name']
                        user.save()
                        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                        return redirect('home')
                else:
                    return render(request, 'accounts/signup.html', {'error': 'Password must be over 8 characters!'})
            else:
                return render(request, 'accounts/signup.html', {'error': 'Passwords Must Match!'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'All fields are required'})
    else:
        return render(request, 'accounts/signup.html')


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        next_url = request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return redirect('home')

