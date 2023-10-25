from django.test import TestCase

# Create your tests here.
class BookTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        # self.assertContains(response, "h1")