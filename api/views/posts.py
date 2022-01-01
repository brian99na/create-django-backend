from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..serializers.post import PostSerializer
from ..models.post import Post

class PostsView(APIView):
    def post(self, request):
        request.data['user'] = request.user.id
        post = PostSerializer(data=request.data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        post = Post.objects.filter(user=request.user.id)
        data = PostSerializer(post, many=True).data
        return Response(data)

class PostView(APIView):
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.user:
            raise PermissionDenied('You cannot delete this post')
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.user != post.user: 
            raise PermissionDenied('You cannot edit this post')
        request.data['user'] = request.user.id
        updated_post = PostSerializer(post, data=request.data)
        if updated_post.is_valid():
            updated_post.save()
            return Response(updated_post.data)
        return Response(updated_post.errors, status=status.HTTP_400_BAD_REQUEST)

class AllView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        posts = Post.objects.all()
        data = PostSerializer(posts, many=True).data
        return Response(data)

class UserPostsView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, pk):
        posts = Post.objects.filter(user=pk)
        print(posts)
        data = PostSerializer(posts, many=True).data
        return Response(data)

class SingleView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, user_pk, pk):
        post = Post.objects.get(user=user_pk, pk=pk)
        post_data = PostSerializer(post).data
        return Response(post_data)
