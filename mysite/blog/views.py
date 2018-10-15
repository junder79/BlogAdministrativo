from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Importamos los Post 
from .models import Post
# Create your views here.
def post_list(request):
	# Se van agregar los post a la platilla.html
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#Detalle del Post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#Vista del formulario
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#Guardar el formulario
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
#Editar el Formulario y guardarlo
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None , request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#Eliminar POST
def post_delete (request , pk):
    post=Post.objects.get(pk=pk)
    if request.method =="POST":
        post.delete()
        return redirect ('/')
    return render(request, 'blog/post_delete.html', {'post': post})
#Formulario de contacto
def post_contacto(request):
    return render(request, 'blog/post_contacto.html', {})