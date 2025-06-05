from django.urls import path
from . import views

"""
Stores the urls paths for the user
"""

app_name = 'user_auth'
urlpatterns = [
  path('', views.user_login, name='login'),
  path('authenticate_user/', views.authenticate_user, name="authenticate_user"),
]
