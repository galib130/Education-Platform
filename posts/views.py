from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from posts.models import Post,Comment
from django.http import Http404,HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from braces.views import SelectRelatedMixin
from django.contrib.auth.decorators import login_required

from .import models
from .import forms


from django.contrib.auth import get_user_model
from posts.forms import CommentForm

User=get_user_model()

class PostList(SelectRelatedMixin,generic.ListView):
    model=models.Post
    select_related=('user','group')

class UserPosts(generic.ListView):
    model=models.Post
    template_name ='posts/user_post_list.html'

    def  get_queryset(self):
        try:
            self.post_user =User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user 
             
       
        return context
       
class PostDetail(SelectRelatedMixin,generic.DetailView):
    model=models.Post
    select_related=('user','group')

    
    def  get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
  

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields=('question','group','video','image')
    model=models.Post

    def form_valid(self,form):
        self.object= form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model=models.Post
    select_related=('user','group')
    success_url=reverse_lazy('posts:all')
    def  get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
        

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('posts:single',pk=post.pk,username=post.user.username)

    else:
        form=CommentForm()
    return render(request,'posts/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    comment.approve()
    post_pk=comment.post.pk
    return redirect('posts:single',pk=post_pk,username=comment.post.user.username)


@login_required
def comment_remove(request,pk):
    comment =get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('posts:single',pk=post_pk,username=comment.post.user.username)

@login_required
def LikePost(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.likes.add(request.user)
    stuff=get_object_or_404(Comment,pk=pk)
    total_likes=stuff.total_likes()
    request.session['total_likes']=total_likes
    post_pk=comment.post.pk
    return redirect('posts:single',pk=post_pk,username=comment.post.user.username)




