from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login
from .models import *


# Register the user
def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, form.save())

      return redirect('../')
  else:
    form = RegisterForm()

  return render(request, "register/register.html", { "form": form })
