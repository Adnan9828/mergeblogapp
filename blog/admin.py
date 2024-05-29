import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Post, User, Catagory, Tags, Comment, Reply

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="post.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Title', 'Author', 'Published Date', 'Thumbnail', 'Feature', 'Category', 
        'User Name', 'First Name', 'Last Name', 'Email', 'City', 'State', 'Image', 
        'Category Name', 'Tags'
    ])
    
    for post in queryset:
        tags = post.tag.all()
        tags_names = ", ".join([tag.name for tag in tags])
        
        writer.writerow([
            post.title, post.author.username, post.published_date, post.thumbnail, 
            post.feature, post.catagory.name, post.author.username, post.author.first_name, 
            post.author.last_name, post.author.email, post.author.city, post.author.state, 
            post.author.image, post.catagory.name, tags_names
        ])
    
    return response


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'thumbnail', 'feature']
    search_fields = ['title', 'author__username', 'catagory__name']
    list_filter = ['published_date', 'feature', 'catagory']
    actions = [export_csv]



def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="User.csv"'

    writer = csv.writer(response)
    writer.writerow([
             'User Name', 'First Name', 'Last Name', 'Email', 'City', 'State', 'Image', 
        
    ])
    
    for post in queryset:
        writer.writerow([
            post.author.username, post.author.first_name, 
            post.author.last_name, post.author.email,
            post.author.city, post.author.state, 
            post.author.image
        ])
    
    return response

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'image', 'city', 'state']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'city', 'state']
    list_filter = ['city', 'state']
    actions = [export_csv]


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Category.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Category Name'
    ])
    
    for post in queryset:
        writer.writerow([
             Catagory.name
        ])
    
    return response

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    actions = [export_csv]


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Tags.csv"'

    writer = csv.writer(response)
    writer.writerow([
         'Tags'
    ])
    
    for post in queryset:
        # tags = post.tag.all()
        # tags_names = ", ".join([tag.name for tag in tags])
        
        writer.writerow([ 
            Tags.name
        ])
    
    return response

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    actions = [export_csv]


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Comments.csv"'

    writer = csv.writer(response)
    writer.writerow([
         
        'User Name', 'Post Name', 'Comment', 
    ])
    
    for post in queryset:
        
        
        writer.writerow([
             Comment.user, Comment.post, Comment.body
        ])
    
    return response

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'body']
    search_fields = ['user','post','body' ]
    list_filter = ['user','post']
    actions = [export_csv]


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reply.csv"'

    writer = csv.writer(response)
    writer.writerow([
         
        'User Name', 'Post Name', 'Comment', 'Reply'  
    ])
    
    for post in queryset:
        
        
        writer.writerow([
             Reply.user, Reply.post, Reply.comment, Reply.body
        ])
    
    return response

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'body']
    search_fields = ['user','post','comment','body' ]
    list_filter = ['user','post','comment']
    actions = [export_csv]

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Catagory, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)


