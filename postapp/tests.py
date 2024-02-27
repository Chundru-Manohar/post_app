from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.
class Posttest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text = "This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text,'This is a test')

    def testdata(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'home.html')
        self.assertContains(response,"This is a test")