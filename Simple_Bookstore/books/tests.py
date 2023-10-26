from django.test import TestCase
from django.contrib.auth.models import User
from .models import Book

# Create your tests here.
# class BookTest(TestCase):
#     def test_url_exists_at_correct_location(self):
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 302)
        # self.assertContains(response, "h1")

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username = "testuser",
            email = "test@test.de",
            password = "1234secret",
        )
        cls.book = Book.objects.create(
            title = "Testbook",
            author = "testauthor",
            description = "Test...",
            published_date = "1990-10-01",
            price = 12.99,
        )
    def test_book_creation(self):
        self.assertEqual(self.book.title, "Testbook")
        self.assertEqual(self.book.author, "testauthor")
        self.assertEqual(self.book.description, "Test...")
        self.assertEqual(self.book.published_date, "1990-10-01")
        self.assertEqual(self.book.price, 12.99)
    
    def test_book_retrieval(self):
         book_from_db = Book.objects.get(pk=1)
         self.assertEqual(book_from_db, self.book)

    def test_book_update(self):
         self.book.title = "An updated title"
         self.book.save()
         self.assertEqual(self.book.title, "An updated title")

    def test_str_representation(self):
         self.assertEqual(self.book.__str__(), 'Testbook')

    def test_book_get_absolute_url(self):
         # Assuming you've defined a get_absolute_url method on the Book model that returns "/book/1/"
         self.assertEqual(self.book.get_absolute_url(), f'/book/{self.book.id}')

    def test_book_deletion(self):
         #book_id = self.book.id
         self.book.delete()
         with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=1)