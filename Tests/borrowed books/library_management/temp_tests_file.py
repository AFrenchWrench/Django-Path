from django.test import TestCase
from .models import Member, Book, Borrowed


class MemberTest(TestCase):
    def setUp(self):
        behdad = Member.objects.create(first_name="Behdad", last_name="Sayadi")
        soroush = Member.objects.create(first_name="Soroush", last_name="Zabihi")

        tokyo_ghoul = Book.objects.create(title="Tokyo Ghoul", genre="Manga")
        berserk = Book.objects.create(title="Berserk", genre="Manga")

        art_of_war = Book.objects.create(title="Art Of War", genre="Idk")
        mein_kampf = Book.objects.create(title="Mein Kampf", genre="Idk")

        fnaf = Book.objects.create(title="FNAF", genre="Horror")

        harry_potter = Book.objects.create(title="Harry Potter", genre="Magic")

        Borrowed.objects.create(member=behdad, book=tokyo_ghoul)
        Borrowed.objects.create(member=behdad, book=berserk)

        Borrowed.objects.create(member=soroush, book=art_of_war)
        Borrowed.objects.create(member=soroush, book=mein_kampf)
        Borrowed.objects.create(member=soroush, book=harry_potter)

    def test_borrowed_books(self):
        soroush = Member.objects.get(first_name="Soroush")
        behdad = Member.objects.get(first_name="Behdad")
        self.assertEqual(
            [Book.objects.get(title="Harry Potter").pk], soroush.borrowed_books("Magic")
        )
        self.assertEqual([], soroush.borrowed_books("Manga"))
        self.assertEqual([], behdad.borrowed_books("Magic"))
