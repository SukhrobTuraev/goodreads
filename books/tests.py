from django.test import TestCase
from django.urls import reverse
from books.models import Book


class BooksTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse('books:books-list'))

        self.assertContains(response, "No books found.")

    def test_books_list(self):
        Book.objects.create(title='Book1', description='description1', isbn='111111')
        Book.objects.create(title='Book2', description='description2', isbn='222222')
        Book.objects.create(title='Book3', description='description3', isbn='333333')

        response = self.client.get(reverse('books:books-list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title='Book1', description='description1', isbn='111111')

        response = self.client.get(reverse('books:books-detail', kwargs={'id': book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)




