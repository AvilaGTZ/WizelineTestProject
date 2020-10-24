from django.test import TestCase
from django.urls import reverse


class TestSetup(TestCase):

    def setUp(self):
        self.indexUrl = reverse('EndPoints:index')
        self.recipeUrl = reverse('EndPoints:recipe')


        return super().setUp()

    def teraDown(self):
        return super().teraDown()


class TesViews(TestSetup):
    def test_Index(self):
        res = self.client.get(self.indexUrl)
        self.assertEqual(res.status_code, 200)

    def test_Recipe(self):
        res = self.client.get(self.recipeUrl)
        self.assertEqual(res.status_code, 302)

