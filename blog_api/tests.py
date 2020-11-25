from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Post, Category
from django.contrib.auth.models import User


class PostTests(APITestCase):
    # Can we make a post from our API

    def test_view_posts(self):
        url = reverse('blog_api:listcreate')
        # client = browser
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_post(self):
        self.test_category = Category.objects.create(name='django')

        self.testuser1 = User.objects.create_user(username='test_user1', password='password')

        data = {"title": "new", "author": 1, "excerpt": "new", "content": "new"}
        url = reverse('blog_api:listcreate')
        response = sef.client.post(url, data, format='json')
        self.asserEqual(response.status_code, status.HTTP_201_CREATED)


