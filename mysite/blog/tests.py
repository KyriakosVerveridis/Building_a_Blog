from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Post
from blog.forms import CommentForm

# from blog.forms import PostForm

# --------------------------
# Models Tests
# --------------------------
# class PostModelTest(TestCase):
#     def test_create_post(self):
#         post = Post.objects.create(title="Hello", content="World")
#         self.assertEqual(post.title, "Hello")
#         self.assertEqual(post.content, "World")

# --------------------------
# Views Tests
# --------------------------
class StartingPageViewTest(TestCase):
    def test_starting_page_status_code(self):
        url = reverse("starting-page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class PostsPageViewTest(TestCase):
    def test_posts_page_status_code(self):
        url = reverse("posts-page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

class SinglePostViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="My First Post",
            slug="my-first-post",
            content="Test content",
            image=SimpleUploadedFile(name='test_image.jpg',
                                     content=b'file_content',
                                     content_type='image/jpeg')
        )

    def test_single_post_page_status_code(self):
        url = reverse("post-detail-page", args=[self.post.slug])
        response = self.client.get(url)


# --------------------------
# Models Tests
# --------------------------
from blog.models import Post, Comment

class PostModelTest(TestCase):
    def test_create_post(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Content here",
            image=SimpleUploadedFile(name='test_image.jpg',
                                     content=b'file_content',
                                     content_type='image/jpeg')
        )
        self.assertEqual(post.title, "Test Post")
        self.assertEqual(post.slug, "test-post")
        self.assertEqual(post.content, "Content here")

class CommentModelTest(TestCase):
    def test_create_comment(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            content="Content here",
            image=SimpleUploadedFile(name='test_image.jpg',
                                     content=b'file_content',
                                     content_type='image/jpeg')
        )
        comment = Comment.objects.create(
            post=post,
            user_name="Tester"
        )
        self.assertEqual(comment.user_name, "Tester")
        self.assertEqual(comment.post, post)
