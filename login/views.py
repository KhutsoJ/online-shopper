from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def user_login(request):
    return render(request, 'authentication/login.html')


# Check if user typed the rigth credentials
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        # return reverse('store')
        return HttpResponseRedirect(
            reverse('store:store')
        )

