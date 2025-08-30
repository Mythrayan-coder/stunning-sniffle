from django.urls import path
from .import views

urlpatterns = [
  #  path('', include('your_app.urls')),  # Replace 'yourappname' with actual app name
  #path("", views.reviews),
  #path("thank-you", views.thank_you),
  path("login", views.chepak_login, name="chepak_login"),
  path("submitted", views.register),
  path("welcome", views.welcome),
  path("final", views.final),
  path("", views.log),
  
  
]