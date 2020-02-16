from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView 

# Create your views here.
#Home: this views display the list of post
class IndexView(ListView):
    template_name='Blog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.all()
    