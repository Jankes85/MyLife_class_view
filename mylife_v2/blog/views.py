from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from calendar import HTMLCalendar
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView, DeleteView, CreateView, UpdateView, DetailView
from .forms import BlogModelForm, BlogPostSearch
from .models import Blog


class PostCreateView(CreateView):
    model = Blog
    form_class = BlogModelForm
    template_name = "blog/create_post.html"
    success_url = reverse_lazy('blog:post_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Add post"
        return context


class PostDetailView(DetailView):
    model = Blog
    template_name = 'blog/post_details.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Blog, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Post"
        return context


class PostUpdateView(UpdateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'blog/create_post.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Blog, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Edit post"
        return context

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "blog.delete_blog"
    model = Blog
    template_name = "blog/post_delete_form.html"
    success_url = reverse_lazy("blog:calendar_current")

    def get_cancel_url(self):
        return reverse("blog:post_detail", args=[self.kwargs["pk"]])


class BlogPostSearchView(FormView):
    template_name = 'blog/search.html'
    form_class = BlogPostSearch

    def form_valid(self, form):
        search_content = form.cleaned_data['search_content']
        entry_date_from = form.cleaned_data['entry_date_from']
        entry_date_to = form.cleaned_data['entry_date_to']
        category = form.cleaned_data['category']
        author = form.cleaned_data['author']

        blog = Blog.objects.all()

        if search_content:
            blog = blog.filter(Q(title__icontains=search_content) | Q(note__icontains=search_content))

        if entry_date_from:
            blog = blog.filter(entry_date__gte=entry_date_from)

        if entry_date_to:
            blog = blog.filter(entry_date__lte=entry_date_to)

        if category:
            blog = blog.filter(category__exact=category)

        if author:
            blog = blog.filter(author__exact=author)

        ctx = {'blog': blog,
               'form': form,
               'site_name': "Search"}

        return super().form_valid(form)



def calendar_current(request):
    month = datetime.now().month
    year = datetime.now().year
    cal = HTMLCalendar().formatmonth(year, month)
    days = []
    for i in range(1, 32):
        try:
            day = date(int(year), int(month), int(i))
            days.append(day)
        except ValueError:
            break

    blog = Blog.objects.all()

    blog_l = []
    for day in days:
        blog_date = Blog.objects.filter(entry_date=day).values()
        blog_l.append(blog_date)

    date_blog_dict = [{k: v} for k, v in zip(days, blog_l)]

    prev = None
    next = None

    if month > 1:
        prev = f'{year}/{month - 1}'
    elif month == 1:
        prev = f"{year - 1}/{month + 11}"

    if month < 12:
        next = f'{year}/{month + 1}'
    elif month == 12:
        next = f"{year + 1}/{month - 11}"

    ctx = {"year": year,
           "month": month,
           "cal": cal,
           "prev": prev,
           "next": next,
           "days": days,
           "blog": blog,
           "blog_l": blog_l,
           "date_blog_dict": date_blog_dict,
           'site_name': "Blog",
           }
    return render(request=request, template_name="blog/calendar_current.html", context=ctx)


def calendar_change(request, year, month):
    month = month
    year = year
    cal = HTMLCalendar().formatmonth(year, month)
    days = []
    for i in range(1, 32):
        try:
            day = date(int(year), int(month), int(i))
            days.append(day)
        except ValueError:
            break

    blog = Blog.objects.all()

    blog_l = []
    for day in days:
        blog_date = Blog.objects.filter(entry_date=day).values()
        blog_l.append(blog_date)

    date_blog_dict = [{k: v} for k, v in zip(days, blog_l)]

    prev = None
    next = None

    if month > 1:
        prev = f'{year}/{month - 1}'
    elif month == 1:
        prev = f"{year - 1}/{month + 11}"

    if month < 12:
        next = f'{year}/{month + 1}'
    elif month == 12:
        next = f"{year + 1}/{month - 11}"

    ctx = {"year": year,
           "month": month,
           "cal": cal,
           "prev": prev,
           "next": next,
           "days": days,
           "blog": blog,
           "blog_l": blog_l,
           "date_blog_dict": date_blog_dict,
           'site_name': "Blog"
           }
    return render(request=request, template_name="blog/calendar_current.html", context=ctx)
