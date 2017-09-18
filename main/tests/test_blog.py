import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from ..models import Post


class BlogViewTests(TestCase):
    def test_blog(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
        )
        url = reverse('main:blog')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.slug)
        self.assertContains(response, new_post.teaser)

    def test_blog_post(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
        )
        url = reverse('main:blog_post', args=[new_post.slug])
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.body)

    def test_featured_blog_post(self):
        new_user = User.objects.create(
            username = 'tester',
            password = 'qwe123!@#',
        )
        new_post = Post.objects.create(
            date = datetime.datetime.now(),
            title = 'New post title',
            slug = 'new-post-slug',
            author = new_user,
            teaser = 'Teaser text',
            body = 'Post body, lots of words',
            is_featured = True,
        )
        url = reverse('main:index')
        response = self.client.get(url)
        self.assertContains(response, 'OK!Thess')
        self.assertContains(response, new_post.title)
        self.assertContains(response, new_post.teaser)
