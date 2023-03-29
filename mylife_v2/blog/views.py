from django.shortcuts import render

# Create your views here.
from datetime import datetime, date

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from calendar import HTMLCalendar
from .forms import BlogModelForm, BlogPostSearch
from .models import Blog


@login_required
def post_create(request):
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            pass
            obj = Blog.objects.create(**form.cleaned_data)
            return redirect('post_detail', id=obj.id)
    else:
        form = BlogModelForm()
        ctx = {'form': form,
               'site_name': "Add post"}
    return render(request=request, template_name='blog/create_post.html', context=ctx)


def post_edit(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogModelForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.note = form.cleaned_data['note']
            post.entry_date = form.cleaned_data['entry_date']
            post.category = form.cleaned_data['category']
            post.author = form.cleaned_data['author']
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        initial = {'title': post.title, 'note': post.note, 'entry_date': post.entry_date, 'category': post.category,
                   'author': post.author}
        form = BlogModelForm(initial=initial)
        ctx = {'form': form,
               'site_name': "Edit post"}
    return render(request=request, template_name='blog/create_post.html', context=ctx)


def post_delete(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('calendar_current')
    ctx = {"post": post,
           'site_name': "Blog"}
    return render(request=request, template_name='blog/post_delete_form.html', context=ctx)


def blog_post_search(request):
    blog = Blog.objects.all()
    form = BlogPostSearch(request.GET)
    if form.is_valid():
        if "search_content" in form.cleaned_data:
            blog = Blog.objects.filter(Q(title__icontains=form.cleaned_data['search_content']) |
                                       Q(note__icontains=form.cleaned_data['search_content']))
        # if "entry_date_from" in form.cleaned_data:
        #     blog = Blog.objects.filter(entry_date__gte=form.cleaned_data['entry_date_from'])
        # if "entry_date_to" in form.cleaned_data:
        #     blog = Blog.objects.filter(entry_date__lte=form.cleaned_data['entry_date_to'])
        # if "category" in form.cleaned_data:
        #     blog = Blog.objects.filter(category=form.cleaned_data['category'])
        # if "author" in form.cleaned_data:
        #     blog = Blog.objects.filter(author=form.cleaned_data['author'])

    form = BlogPostSearch()
    ctx = {'blog': blog,
           'form': form,
           'site_name': "Search"}
    return render(request=request, template_name='blog/search.html', context=ctx)


def post_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    ctx = {'post': post,
           'site_name': "Post"}
    return render(request=request, template_name='blog/post_details.html', context=ctx)


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
