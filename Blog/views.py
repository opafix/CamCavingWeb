from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import ImageForm, PostForm
from .models import *
from datetime import datetime
from django.shortcuts import get_object_or_404, Http404
from django.views.generic.list import ListView

class Blog(ListView):
    model = Post
    template_name = 'Meets/Blog.html'
    paginate_by = 5
    context_obect_name = 'post_list'
    queryset = Post.objects.all().order_by('-published_date')

@permission_required('Blog.add_post', login_url='/Portal/login')
def BlogPost(request):
    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=10)
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.save()
            for form in formset.cleaned_data:
                #this helps to not crash if the user
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = Image(post=post_form, images=image)
                    photo.save()
            messages.success(request,"Success")
            return redirect("/Blog")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'Blog/Post.html', {'postForm': postForm, 'formset': formset})

@permission_required('Blog.change_post', login_url='/Portal/login')
def BlogEdit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/Blog', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Blog/Edit.html', {'form': form})

@permission_required('Blog.delete_post', login_url='/Portal/login')
def BlogDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user and not request.user.is_superuser:
        raise Http404("You are not allowed to delete this Post")
    post.delete()
    return redirect('/Blog')
