from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


def get_queryset(query):
    return query.select_related(
        'category',
        'location',
        'author'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True)


def index(request):
    templates = 'blog/index.html'
    posts = get_queryset(Post.objects).order_by('-pub_date')[:5]
    context = {'posts': posts}
    return render(request, templates, context)


def post_detail(request, post_id):
    templates = 'blog/detail.html'
    post = get_object_or_404(get_queryset(Post.objects), pk=post_id)
    context = {'post': post}
    return render(request, templates, context)


def category_posts(request, category_slug):
    templates = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    posts = get_queryset(category.post_list)
    context = {
        'category': category,
        'post_list': posts}
    return render(request, templates, context)
