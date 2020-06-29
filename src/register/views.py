from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout

from .forms import RegisterForm

# Create your views here.
def register(request):
	request.user
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect("/login")
	else:
		form = RegisterForm()
	
	return render(request, "register/register.html", {"form": form})