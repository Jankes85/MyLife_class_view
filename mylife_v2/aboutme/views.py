from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from .forms import ContactForm
from .models import Experience, Education, Course, Book, Skill, Language
from django.core.mail import send_mail, BadHeaderError

# Create your views here.



class AboutMeView(TemplateView):
    template_name = "aboutme/aboutme.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "About me"
        return context


class EducationView(ListView):
    model = Education
    fields = "__all__"
    template_name = "aboutme/education.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['books'] = Book.objects.all()
        context['site_name'] = "Education"
        return context


class ExperienceView(ListView):
    model = Experience
    fields = "__all__"
    template_name = "aboutme/experience.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Experience"
        return context


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            request.session["first_name"] = form.cleaned_data["first_name"]
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("aboutme:thanks")
    else:
        form = ContactForm()

    ctx = {"form": form,
           'site_name': "Contact",
           }
    return render(request=request, template_name="aboutme/contact.html", context=ctx)


class ContactView(FormView):
    template_name = "aboutme/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("aboutme:thanks")

    def form_valid(self, form):
        email_content = form.get_email_content()
        send_mail(
            'Contact form submission',
            email_content,
            'sender@example.com',
            ['recipient@example.com'],
            fail_silently=False,
        )
        self.request.session['first_name'] = form.cleaned_data.get('first_name', '')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Contact"
        return context


class SkillsView(ListView):
    model = Language
    fields = "__all__"
    template_name = "aboutme/skills.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills_s'] = Skill.objects.filter(skill_type="s")
        context['skills_t'] = Skill.objects.filter(skill_type="t")
        context['site_name'] = "Skills"
        return context


class ThanksView(TemplateView):
    template_name = "aboutme/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_name'] = self.request.session['first_name']
        context['site_name'] = "Contact"
        return context



class PythonView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="python")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="python")
        context['books'] = Book.objects.filter(competences__icontains="python")
        context['site_name'] = "Python"
        context['skill'] = "Python"
        return context


class SqlView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="sql")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="sql")
        context['books'] = Book.objects.filter(competences__icontains="sql")
        context['site_name'] = "SQL"
        context['skill'] = "SQL"
        return context


class DjangoView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="django")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="django")
        context['books'] = Book.objects.filter(competences__icontains="django")
        context['site_name'] = "Django"
        context['skill'] = "Django"
        return context


class HtmlView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="html")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="html")
        context['books'] = Book.objects.filter(competences__icontains="html")
        context['site_name'] = "HTML"
        context['skill'] = "HTML"
        return context


class CssView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="css")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="css")
        context['books'] = Book.objects.filter(competences__icontains="css")
        context['site_name'] = "CSS"
        context['skill'] = "CSS"
        return context


class JsView(ListView):
    template_name = "aboutme/from_where_skills.html"
    queryset = Education.objects.filter(competences__icontains="javascript")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(competences__icontains="javascript")
        context['books'] = Book.objects.filter(competences__icontains="javascript")
        context['site_name'] = "JavaScript"
        context['skill'] = "JavaScript"
        return context

