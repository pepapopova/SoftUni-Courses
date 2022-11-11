from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    NAME = 'Google'

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test_if_innit_gives_proper_result(self):
        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_if_setter_raises_error_when_name_is_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(error.exception))
        self.assertEqual(self.NAME, self.library.name)

    def test_add_book_when_author_and_title_not_in_books_by_author_dict(self):
        author = 'Paulo Coehlo'
        title = 'Green book'
        self.library.add_book(author, title)
        self.assertEqual([title], self.library.books_by_authors[author])

    def test_add_book_when_title_not_in_books_by_author_dict(self):
        author = 'Paulo Coehlo'
        title = 'Green book'
        title2 = 'The predator'
        self.library.add_book(author, title)
        self.library.add_book(author, title2)
        self.assertEqual([title, title2], self.library.books_by_authors[author])

    def test_add_reader_when_reader_is_new(self):
        name = 'Pepa'
        self.library.add_reader(name)
        self.assertEqual([], self.library.readers[name])
        self.assertTrue(name in self.library.readers)

    def test_add_reader_when_reader_is_already_in_the_dict(self):
        name = 'Pepa'
        self.library.add_reader(name)
        result = self.library.add_reader(name)
        self.assertEqual(f"{name} is already registered in the {self.NAME} library.", result)
        self.assertTrue(name in self.library.readers)

    def test_rent_book_when_reader_not_in_readers_dict(self):
        reader = 'Pepa'
        book_author = 'James Sawyer'
        book = 'The predator'
        result = self.library.rent_book(reader, book_author, book)
        self.assertEqual(f"{reader} is not registered in the {self.NAME} Library.", result)
        self.assertFalse(reader in self.library.readers)

    def test_rent_book_when_author_not_in_authors_dict(self):
        reader = 'Pepa'
        book_author = 'James Sawyer'
        book = 'The predator'
        self.library.add_reader(reader)
        result = self.library.rent_book(reader, book_author, book)
        self.assertEqual(f"{self.NAME} Library does not have any {book_author}'s books.", result)

    def test_rent_book_tittle_not_in_authors_dict(self):
        reader = 'Pepa'
        book_author = 'James Sawyer'
        book = 'The predator'
        self.library.add_reader(reader)
        self.library.books_by_authors[book_author] = []
        result = self.library.rent_book(reader, book_author, book)
        self.assertEqual(f"""{self.NAME} Library does not have {book_author}'s "{book}".""", result)

    def test_rent_book__when_reader_author_and_title_are_intact(self):
        reader = 'Pepa'
        book_author = 'James Sawyer'
        book = 'The predator'
        self.library.add_reader(reader)
        self.library.books_by_authors[book_author] = [book]
        self.library.rent_book(reader, book_author, book)
        self.assertEqual([{book_author: book}], self.library.readers[reader])
        self.assertTrue(book not in self.library.books_by_authors[book_author])


if __name__ == "__main__":
    main()