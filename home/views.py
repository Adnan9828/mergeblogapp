from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import User, Catagory, Tags, Post, Comment, Reply
from .serializers import UserSerializer, CatagorySerializer, TagsSerializer, PostSerializer, CommentSerializer, ReplySerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home(request, id=None):
    if request.method == 'GET':
        if id:
            user = get_object_or_404(User, id=id)
            serializer = UserSerializer(user)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response({'status': 200, 'payload': serializer.data})
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({'status': 204, 'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home1(request, slug=None):
    if request.method == 'GET':
        if slug:
            catg = get_object_or_404(Catagory, slug=slug)
            serializer = CatagorySerializer(catg)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            catg = Catagory.objects.all()
            serializer = CatagorySerializer(catg, many=True)
            return Response({'status': 200, 'payload': serializer.data})

    if request.method == 'POST':
        serializer = CatagorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        catg = get_object_or_404(Catagory, slug=slug)
        serializer = CatagorySerializer(catg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        catg = get_object_or_404(Catagory, slug=slug)
        serializer = CatagorySerializer(catg, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        catg = get_object_or_404(Catagory, slug=slug)
        catg.delete()
        return Response({'status': 204, 'message': 'Category deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home2(request, slug=None):
    if request.method == 'GET':
        if slug:
            tag = get_object_or_404(Tags, slug=slug)
            serializer = TagsSerializer(tag)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            tag = Tags.objects.all()
            serializer = TagsSerializer(tag, many=True)
            return Response({'status': 200, 'payload': serializer.data})

    if request.method == 'POST':
        serializer = TagsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        tag = get_object_or_404(Tags, slug=slug)
        serializer = TagsSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        tag = get_object_or_404(Tags, slug=slug)
        serializer = TagsSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        tag = get_object_or_404(Tags, slug=slug)
        tag.delete()
        return Response({'status': 204, 'message': 'Tag deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home3(request, slug=None):
    if request.method == 'GET':
        if slug:
            post = get_object_or_404(Post, slug=slug)
            serializer = PostSerializer(post)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            post = Post.objects.all()
            serializer = PostSerializer(post, many=True)
            return Response({'status': 200, 'payload': serializer.data})
    
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return Response({'status': 204, 'message': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home4(request, sno=None):
    if request.method == 'GET':
        if id:
            comm = get_object_or_404(Comment, sno=sno)
            serializer = CommentSerializer(comm)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            comm = Comment.objects.all()
            serializer = CommentSerializer(comm, many=True)
            return Response({'status': 200, 'payload': serializer.data})
        
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        comm = get_object_or_404(Comment, sno=sno)
        serializer = CommentSerializer(comm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        comm = get_object_or_404(Comment, sno=sno)
        serializer = CommentSerializer(comm, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        comm = get_object_or_404(Comment, sno=sno)
        comm.delete()
        return Response({'status': 204, 'message': 'Comment deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def home5(request, sno=None):
    if request.method == 'GET':
        if sno:
            reply = get_object_or_404(Reply, sno=sno)
            serializer = ReplySerializer(reply)
            return Response({'status': 200, 'payload': serializer.data})
        else:
            reply = Reply.objects.all()
            serializer = ReplySerializer(reply, many=True)
            return Response({'status': 200, 'payload': serializer.data})
        
    if request.method == 'POST':
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        reply = get_object_or_404(Reply, sno=sno)
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        reply = get_object_or_404(Reply, sno=sno)
        serializer = ReplySerializer(reply, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        reply = get_object_or_404(Reply, sno=sno)
        reply.delete()
        return Response({'status': 204, 'message': 'Reply deleted'}, status=status.HTTP_204_NO_CONTENT)
