from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from usersapp.forms import UserRegisterForm, UserLoginForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:main')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'usersapp/signupuser.html', {'form': form})
    return render(request, 'usersapp/signupuser.html', context={'form': UserRegisterForm()})


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotesapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect(to='usersapp:loginuser')

        login(request, user)
        return redirect(to='quotesapp:main')

    return render(request, 'usersapp/loginuser.html', context={'form': UserLoginForm()})


@login_required()
def logoutuser(request):
    logout(request)
    return redirect(to='quotesapp:main')
