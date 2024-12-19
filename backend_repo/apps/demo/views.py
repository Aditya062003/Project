import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Comment, Post, User
from .serializers import CommentSerializer, PostSerializer, UserSerializer


class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfinitePostListView(APIView, PageNumberPagination):
    page_size = 10

    def get(self, request):
        posts = Post.objects.all().order_by("-timestamp")
        results = self.paginate_queryset(posts, request, view=self)

        response_data = []
        for post in results:
            comments = post.comments.all().order_by("-timestamp")[:3]
            response_data.append(
                {
                    "id": str(post.id),
                    "text": post.text,
                    "timestamp": post.timestamp,
                    "author": post.user.username,
                    "comment_count": post.comments.count(),
                    "comments": [
                        {
                            "text": comment.text,
                            "timestamp": comment.timestamp,
                            "author": comment.user.username,
                        }
                        for comment in comments
                    ],
                }
            )
        return self.get_paginated_response(response_data)


class CreatePostView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, id=request.data.get("user"))
            post = serializer.save(user=user)
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePostView(APIView):
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeletePostView(APIView):
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response(
            {"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class CreateCommentView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, id=request.data.get("user"))
            serializer.save(post=post, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllCommentsListView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all().order_by("-timestamp")
        response_data = [
            {
                "text": comment.text,
                "timestamp": comment.timestamp,
                "author": comment.user.username,
            }
            for comment in comments
        ]
        return Response(response_data, status=status.HTTP_200_OK)


class RandomCommentListView(APIView):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all()
        random_comments = random.sample(list(comments), min(3, len(comments)))
        response_data = [
            {
                "text": comment.text,
                "timestamp": comment.timestamp,
                "author": comment.user.username,
            }
            for comment in random_comments
        ]
        return Response(response_data, status=status.HTTP_200_OK)
