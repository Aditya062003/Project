import uuid

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Comment, Post, User


class TestAPIViews(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(
            username="testuser", email="testuser@example.com"
        )
        # Create a test post
        self.post = Post.objects.create(text="Test post", user=self.user)
        # Create test comments
        self.comment1 = Comment.objects.create(
            text="Test comment 1", post=self.post, user=self.user
        )
        self.comment2 = Comment.objects.create(
            text="Test comment 2", post=self.post, user=self.user
        )

    def test_create_user(self):
        url = reverse("create_user")
        data = {"username": "newuser", "email": "newuser@example.com"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_infinite_posts(self):
        url = reverse("infinite_posts")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)

    def test_create_post(self):
        url = reverse("create_post")
        data = {"text": "New post", "user": str(self.user.id)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post(self):
        url = reverse("update_post", args=[self.post.id])
        data = {"text": "Updated post"}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.text, "Updated post")

    def test_delete_post(self):
        url = reverse("delete_post", args=[self.post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_create_comment(self):
        url = reverse("create_comment", args=[self.post.id])
        data = {"text": "New comment", "user": str(self.user.id)}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_all_comments(self):
        url = reverse("all_comments", args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_random_comments(self):
        url = reverse("random_comments", args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertLessEqual(len(response.data), 3)
