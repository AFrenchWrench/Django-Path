from django.test import TestCase
from .models import Book


class TestAPI(TestCase):
    def setUp(self):
        tokyo_ghoul = Book.objects.create(title="Tokyo Ghoul", genre="Manga")
        berserk = Book.objects.create(title="Berserk", genre="Manga")

        art_of_war = Book.objects.create(title="Art Of War", genre="Idk")
        mein_kampf = Book.objects.create(title="Mein Kampf", genre="Idk")

        fnaf = Book.objects.create(title="FNAF", genre="Horror")

        harry_potter = Book.objects.create(title="Harry Potter", genre="Magic")

    # tests
    def test_books(self):
        existing_genre = "Manga"
        preferred_response_for_existing_genre = {
            "title": "List of Books",
            "genre": existing_genre,
            "books": [book.pk for book in Book.objects.filter(genre=existing_genre)],
        }
        non_existent_genre = "Tech"
        preferred_response_for_non_existent_genre = {
            "title": "List of Books",
            "genre": non_existent_genre,
            "books": [
                book.pk for book in Book.objects.filter(genre=non_existent_genre)
            ],
        }

        response_existing_genre = self.client.get(f"/books/{existing_genre}/")
        result_existing_genre = response_existing_genre.json()
        self.assertEqual(
            result_existing_genre.get("title"),
            preferred_response_for_existing_genre.get("title"),
        )
        self.assertEqual(
            result_existing_genre.get("genre"),
            preferred_response_for_existing_genre.get("genre"),
        )
        self.assertEqual(
            result_existing_genre.get("books"),
            preferred_response_for_existing_genre.get("books"),
        )

        response_non_existent_genre = self.client.get(f"/books/{non_existent_genre}/")
        result_non_existent_genre = response_non_existent_genre.json()
        self.assertEqual(
            result_non_existent_genre.get("title"),
            preferred_response_for_non_existent_genre.get("title"),
        )
        self.assertEqual(
            result_non_existent_genre.get("genre"),
            preferred_response_for_non_existent_genre.get("genre"),
        )
        self.assertEqual(
            result_non_existent_genre.get("books"),
            preferred_response_for_non_existent_genre.get("books"),
        )
