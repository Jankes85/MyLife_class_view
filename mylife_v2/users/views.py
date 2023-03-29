from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have register successfully.')
            return redirect("aboutme:about_me")
        messages.error(request, 'Data you entered are wrong')
    form = RegistrationForm()
    ctx = {"form": form}
    return render(request=request, template_name="registration/register.html", context=ctx)
