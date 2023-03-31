from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import RegistrationForm


# def register(request):
#     if request.method == "POST":
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'You have register successfully.')
#             return redirect("aboutme:about_me")
#         messages.error(request, 'Data you entered are wrong')
#     form = RegistrationForm()
#     ctx = {"form": form}
#     return render(request=request, template_name="registration/register.html", context=ctx)

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("thanks")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.request.session['first_name'] = form.cleaned_data.get('first_name')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Register"
        return context


class ThanksView(TemplateView):
    template_name = "registration/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Register"
        context['first_name'] = self.request.session['first_name']
        return context

