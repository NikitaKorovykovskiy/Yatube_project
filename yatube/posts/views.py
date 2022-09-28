from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Это главная страница проекта Yatube'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_lists(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = Group.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group': group,
        'postes': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
