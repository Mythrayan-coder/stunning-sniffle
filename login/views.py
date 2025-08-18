from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import ReviewForm,ChepakLoginForm
from django.contrib import messages
from django.shortcuts import render, redirect

def log(request):
    return render(request,"log.html")
      # Use 'request' to match Django's convention

def chepak_login(request):
    if request.method == "POST":
        form = ChepakLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            try:
                user = chepak.objects.get(Email_address=email, Password=password)
            except chepak.DoesNotExist:
                user = None

            if user:
                # Save login state in session
                request.session['chepak_user_id'] = user.id
                messages.success(request, "Login successful.")
                return redirect("welcome/")  # or any view name
            else:
                messages.error(request, "Incorrect email or password.")
    else:
        form = ChepakLoginForm()

    return render(request, "login.html", {"form": form})
       

def register(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Only save the password once—it’s safe now
            instance = form.save(commit=False)  # Optional: but not used
            instance.save()
            return HttpResponseRedirect('/welcome')
    else:
        form = ReviewForm()

    return render(request, 'Submit.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')