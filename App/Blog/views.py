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
# view post detail
class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post-detail.html'

#Create a new post
def postview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request, 'Blog/post.html', {'form':form})

#Edit the post element
def edit(request, pk, template_name='Blog/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or none, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#delete the post element
def delete(request, pk, template_name='Blog/confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object': post})
        
    