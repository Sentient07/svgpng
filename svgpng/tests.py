import unittest
from django.test import Client


class ButtonTestCase(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_details(self):
        print("test..")
        post_response = self.client.post("/", follow=True)
        png_file = open('new-image.png', 'wb+')
        png_file.write(post_response.content)
        self.assertEquals(post_response.get('content-type'),
        "image/png"
        )