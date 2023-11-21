from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category
from django.db.models import Q


NOW_DATE = timezone.now()


def index(request):
    templates = 'blog/index.html'
    posts = Post.objects.filter(
        pub_date__lte=NOW_DATE,
        is_published=True,
        category__is_published=True,
    ).order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, templates, context)


def post_detail(request, post_id):
    templates = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            Q(pub_date__lte=NOW_DATE)
            & Q(is_published=True)
            & Q(category__is_published=True)
        ), pk=post_id
    )
    context = {'post': post}
    return render(request, templates, context)


def category_posts(request, category_slug):
    templates = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__gte=NOW_DATE
    )
    context = {
        'category': category,
        'posts': posts}
    return render(request, templates, context)
