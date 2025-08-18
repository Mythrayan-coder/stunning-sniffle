from django.urls import path, include

urlpatterns = [
  #  path('', include('your_app.urls')),  # Replace 'yourappname' with actual app name
  #path("", include("reviews.urls"))
  path("",include("login.urls")),
]
