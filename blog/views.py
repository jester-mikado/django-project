from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post

# Create your views here.
    # blog_title = "latest news"
    # posts = [
    #     {'id':1, 'title': 'meoww'},
    #     {'id':2, 'title': 'british'},
    #     {'id':3, 'title': 'nigga'},
    #     {'id':4, 'title': 'bitch'},
    #     {'id':5, 'title': 'japanesuuuu'},
    # ]
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',{'posts': posts})

def details(request, post_id):
    # post = next((item for item in posts if item['id'] == int{post_id}), None)
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html',{'post': post})

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse(" neww url")