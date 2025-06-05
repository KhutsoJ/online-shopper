from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import login
from .models import *


# Register the user
def register(request):
  """
  Send a registration form to the user
  if the form is valid, log the user in and
  save the credentials so the user can login
  later. If not, send the form again.

  :param obj request: The user details
  
  :returns: If invalid, will return the register page
  """
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, form.save())

      return redirect('../')
  else:
    form = RegisterForm()

  return render(request, "register/register.html", { "form": form })
