from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from taggit.managers import TaggableManager

# Create your views here.
from mainapp.models import *
from  .models import *
from .forms import BlogCommentsForm



def blog(request):
    blogs = Blog.objects.all().order_by('-date_published')
    popular_blogs = Blog.objects.all().order_by('-hit_count_generic__hits')
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    tag = TaggableManager()

    category = request.GET.get('q')
    if category == None:
        blogs = Blog.objects.all().order_by('-date_published')
    else:
        blogs = Blog.objects.all().filter(blog_category__category=category).order_by('-hit_count_generic__hits')
    categories = BlogCategory.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        blogs = blogs.filter(Q(title__icontains=search) | Q(text__icontains=search))
    else:
        blogs = Blog.objects.all().order_by('-hit_count_generic__hits')
    
    context = {
        'blogs':blogs,
        'categories':categories,
        'popular_blogs':popular_blogs,
        'mainCategory':mainCategory,
        'tag':tag,
        'last_three':last_three,
    }
    return render(request, 'blog/blog.html', context)



def blog_view(request, pk):
    blogs = Blog.objects.get(id=pk)
    category = BlogCategory.objects.all()
    hit_count = HitCount.objects.get_for_object(blogs)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    popular_blogs = Blog.objects.all().order_by('-hit_count_generic__hits')
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    qty_comments = BlogComments.objects.filter(blog_id=blogs).count()

    new_comment=None
    form = BlogCommentsForm()
    if request.method == 'POST':
        form = BlogCommentsForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blogs
            new_comment.save()
            return redirect('blog_view', blogs.id)
        else:
            form = BlogCommentsForm()


    context = {
        'blogs':blogs,
        'category':category,
        'hit_count_response':hit_count_response,
        'popular_blogs':popular_blogs,
        'new_comment':new_comment,
        'form':form,
        'qty_comments':qty_comments,
        'last_three':last_three,
        'mainCategory':mainCategory,
    }
    return render(request, 'blog/single-fullwidth.html', context)
