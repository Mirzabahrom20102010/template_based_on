from django.db import models
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from hitcount.utils import get_hitcount_model

from posts.custom_permission import OnlyLoggedSuperUser
from posts.forms import CommentForm, PostForm
from posts.models import Post, Category, Comment


class CommView(View):
    def get(self, request, id):
        posts =get_object_or_404(Post, id=id)

        comment = Comment.objects.all()
        user_id = Comment.objects.filter(id=id)
        comment_form = CommentForm()

        context = {
            'comments': comment,
            'comment_form':comment_form,
        }

        return render(request, 'detail.html', context)

    def post(self, request, id):
        posts =get_object_or_404(Post, id=id)

        comment = Comment.objects.all()
        user_id = Comment.objects.filter(id=id)
        comment_form = CommentForm()

        if user_id == posts.id:
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.posts = posts
                new_comment.user = request.user
                new_comment.save()
                comment_form = CommentForm()
        context = {
            'comments': comment,
            'comment_form':comment_form,
        }

        return render(request, 'detail.html', context)

class Created_view(OnlyLoggedSuperUser, CreateView):
    model = Post
    fields = ['title', 'slug', 'body', 'category', 'status', 'image', ]
    success_url = reverse_lazy('home_page')
    template_name = 'post/create.html'

class CategoryView(View):
    def get(self, request, id):
        categ = Category.objects.all()
        category = categ.objects.filter(id=id)

        context = {
            'categorys': categ,
            'category': category,
        }

        return render(request, 'home_page.html', context)

class PostView(View):

    def get(self, request):
        posts_all = Post.objects.all()
        post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
        context = {
            'all_posts': posts_all,
            'id': post_id,
        }

        return render(request, 'list.html', context)

class PostDetailView(View):
    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        comments = Comment.objects.filter(posts=id)
        comment_form = CommentForm()
        comment_count = len(comments)
        viewed_posts = request.session.get('viewed_posts', [])
        if id not in viewed_posts:
            post.views += 1
            post.save()

            # Добавляем пост в список просмотренных
            viewed_posts.append(id)
            request.session['viewed_posts'] = viewed_posts

        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'comment_count': comment_count,
        }
        return render(request, "detail.html", context)

    def post(self, request, id):
        posts = Post.objects.get(id=id)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            Comment.objects.create(
                posts=posts,
                user=request.user,
                body=comment_form.cleaned_data['body'],
            )
            return redirect(reverse('posts:post-detail', kwargs={'id': posts.id}))

        context = {
            "poot": posts,
            "comment_form": comment_form
        }
        return render(request, "posts/detail.html", context)


class CreatePostView(CreateView):
    model = Post
    # classform = PostForm
    fields = ['title', 'body', 'category', 'picture']
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:post-list')