# Books/tests.py

import json
from django.test import TestCase, Client
from .models import Book

class BookTests(TestCase):
    def setUp(self):
        
        self.client = Client()
        self.book = Book.objects.create(title="Test Book", author="Test Author")

    def test_book_creation(self):

        payload = {'title': 'New Book', 'author': 'New Author'}
        response = self.client.post(
            '/api/books', 
            data=json.dumps(payload), 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['title'], 'New Book')
        self.assertEqual(response_data['author'], 'New Author')

    def test_book_list_view(self):
        
        response = self.client.get('/api/books') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")
        self.assertContains(response, "Test Author")

    def test_book_detail_view(self):
       
        url = f'/api/books/{self.book.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data['title'], self.book.title)
        self.assertEqual(response_data['author'], self.book.author)