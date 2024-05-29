from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, User, Catagory, Tags, Comment,Reply
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm, UserForm, SignupForm, UserProfileForm, ProfilePhotoForm, CommentForm,ReplyForm
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    for post in posts:
        if post.tag:
            print(post.tag.name, ">>>>>>>>>>>>>>>>>>>")
        else:
            print("No tag associated with post:", post.slug)
    return render(request, "blog/post_list.html", {"posts": posts})


def category(request,slug):
    print(request, '>>>>>>>>>>>>>>>>>>>', slug)
    categories = Post.objects.filter(catagory__slug=slug)
    return render(request, "blog/category.html", {"categories":categories})


def tag(request, slug):
    print(slug)
    if slug:
        tags = Post.objects.filter(tag__slug=slug).order_by("published_date")
    else:
        tags = Post.objects.all().order_by("published_date")
    return render(request, "blog/tag.html", {"tags": tags})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            tags = form.cleaned_data['tag']
            post.tag.set(tags)  # Set the tags for the post
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})
            

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            tags = form.cleaned_data['tag']
            post.tag.set(tags)
            return redirect("post_detail", slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})


def postcomment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post = get_object_or_404(Post, id=request.POST.get('post_id'))
            comment.post = post
            comment.user = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            comment.save()
            return redirect('post_detail', slug=post.slug)
    return redirect('post_list')


def create_reply(request):
    comment = request.POST.get('comment_sno')
    parent_comment = get_object_or_404(Comment, sno=comment)
    # parent_commentr = Comment.objects.get(id=comment)
    post = parent_comment.post
    if request.method == 'POST':
        print(request.POST)
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.post = post
            reply.comment = parent_comment
            reply.user = request.user  
            reply.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = ReplyForm()
    return render(request, 'blog/post_detail.html', {'form': form, 'post': post,'parent_comment': parent_comment,})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post).select_related('user', 'parent')
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'user': request.user,
    })


def user_login(request):
    form = UserForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(username, "uuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
        if user is not None:
            print("yes")
            login(request, user)
            return redirect("/", "Welcome, {}!".format(request.user.username))
    return render(request, "blog/userlogin.html", {"form": form})


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  
            user.save()
            messages.success(request, "Your Account has been successfully created!")
            return redirect("user-login")
    else:
        form = SignupForm()
    return render(request, "blog/usersignup.html", {"form": form})
    

def user_signout(request):
    logout(request)
    return redirect("user-login")


@login_required
def edit_profile(request, user_id):
    user_profile = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_profile_form.is_valid():
            user_profile_form.save()
            messages.success(request, "Your profile has been successfully updated!")
            return redirect("post_list") 
    else:
        user_profile_form = UserProfileForm(instance=user_profile)
    return render(request, "blog/user_edit.html", {"user_profile_form": user_profile_form})


@login_required
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, "blog/user_detail.html", {"user": user})


def upload_profile_photo(request):
    if request.method == "POST":
        form = ProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = ProfilePhotoForm(instance=request.user)
    return render(request, "blog/user_edit.html", {"form": form})


