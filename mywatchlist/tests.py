from django.test import TestCase
from django.test import Client
from django.urls import resolve

# Create your tests here.
class WatchListTest(TestCase):

    def htmlTest(self):
        tes = self.client.get("/mywatchlist/html/")
        self.assertEqual(tes.status_code,200)

    def xmlTest(self):
        tes = self.client.get("/mywatchlist/xml/")
        self.assertEqual(tes.status_code,200)

    def jsonTest(self):
        tes = self.client.get("/mywatchlist/json/")
        self.assertEqual(tes.status_code,200)