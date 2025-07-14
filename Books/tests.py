from django.urls import reverse
from .models import Book
from Library.api import api
from django.test import TestCase, Client

class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Test Author")
        self.client = Client()

    def test_book_creation(self):
        response = self.client.post('/api/books/', {
            'title': 'New Book',
            'author': 'New Author'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], 'New Book')
        self.assertEqual(response.json()['author'], 'New Author')

    def test_book_list_view(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertContains(response, "Test Author")

    def test_book_detail_view(self):
        response = self.client.get('/api/books/{}/'.format(self.book.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], self.book.title)
        self.assertEqual(response.json()['author'], self.book.author)
