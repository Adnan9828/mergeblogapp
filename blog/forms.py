from django import forms

from .models import Post, User,Tags,Comment, Catagory,Reply

from django.contrib.auth import authenticate,login,logout


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text','thumbnail','feature','catagory', 'tag')


class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'username', 'name': 'username'})
    )
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'col-10', 'id': 'password', 'name': 'password'})
    )
    class Meta:
        model = User
        fields = ("username","password")


class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image']

        

class SignupForm(forms.ModelForm):

    
    username=forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={'class': 'col-8', 'id': 'username', 'name': 'username'})
    )

    firstname=forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'col-8', 'id': 'firstname', 'name': 'firstname'}),
    )
    lastname=forms.CharField(
        label='last name',
        widget=forms.TextInput(attrs={'class': 'col-8', 'id': 'lastname', 'name': 'lastname'}),
    )
    
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'col-8', 'id': 'email', 'name': 'email'})
    )
    password=forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'col-8', 'id': 'password', 'name': 'password'})
    )
    repassword=forms.CharField(
        label="Re-Password",
        widget=forms.PasswordInput(attrs={'class': 'col-8', 'id': 'repassword', 'name': 'repassword'})
    )
    city=forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class':'col-8','id':'city','name':'city'})
    )
    state=forms.CharField(
        label="state",
        widget=forms.TextInput(attrs={'class':'col-8','id':'state','name':'state'})
    )
    image=forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file col-8', 'id': 'image', 'name': 'image'})
    )
    class Meta:
        model = User
        fields = ["username","firstname","lastname","email","password","repassword","city","state","image"]


class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(
    label='',
    widget=forms.ClearableFileInput(attrs={'class': 'form-control-file ', 'id': 'image', 'name': 'image'})
    )

    class Meta:
        model = User
        fields = ('image','firstname','lastname','city','state')


class CommentForm(forms.ModelForm):
   
    body=forms.CharField(
        label='Comment',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'body', 'name': 'body'})
    )
    # name=forms.CharField(
    #     label='Name',
    #     widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'name', 'name': 'name'})
    # )
    # email=forms.CharField(
    #     label='Email',
    #     widget=forms.EmailInput(attrs={'class': 'col-10', 'id': 'email', 'name': 'email'})
    # )
    class Meta:
        model = Comment
        fields = ['body',]


class ReplyForm(forms.ModelForm):
     body=forms.CharField(
        label='Reply',
        widget=forms.TextInput(attrs={'class': 'col-10', 'id': 'body', 'name': 'body'})
    )
     class Meta:
        model = Reply
        fields = ['body',]