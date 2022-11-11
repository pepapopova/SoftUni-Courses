from project.bookstore import Bookstore
from unittest import TestCase

class BookstoreTest(TestCase):
    BOOKS_LIMIT = 3
    BOOKS = {'RedHat': 2, 'Pipi': 1}

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

    def test_innit(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_book_limit_setter(self):
        with self.assertRaises(ValueError) as error:
            value = 0
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))

    def test_book_limit_setter_below_zero(self):
        with self.assertRaises(ValueError) as error:
            value = -6
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))

    def test_book_limit_setter_works_properly(self):
        self.bookstore.books_limit = 1
        self.assertEqual(1, self.bookstore.books_limit)

    def test_if_len_works_when_books_available(self):
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS
        self.assertEqual(3, len(self.bookstore))

    def test_len_when_no_books_in_the_bookstore(self):
        self.assertEqual(0, len(self.bookstore))

    def test_when_no_enough_capacity(self):
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Inception', 3)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_when_no_books_but_still_not_capacity(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book('Inception', 4)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_when_capacity_is_enough_and_book_not_in_library(self):
        result = self.bookstore.receive_book('Inception', 2)
        self.assertEqual(f"2 copies of Inception are available in the bookstore.", result)
        self.assertEqual({'Inception': 2}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles['Inception'])

    def test_when_capacity_is_enough_and_book_already_inside(self):
        self.bookstore.availability_in_store_by_book_titles = {'Inception': 2}
        result = self.bookstore.receive_book('Inception', 1)
        self.assertEqual(f"3 copies of Inception are available in the bookstore.", result)
        self.assertEqual({'Inception': 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles['Inception'])

    def test_sell_book_raises_error_when_not_available(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Inception', 2)
        self.assertEqual(f"Book Inception doesn't exist!", str(error.exception))
        self.assertEqual(0, len(self.bookstore))

    def test_sell_book_raises_when_books_not_empty(self):
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Inception', 1)
        self.assertEqual(f"Book Inception doesn't exist!", str(error.exception))
        self.assertEqual(3, len(self.bookstore))

    def test_sel_book_raises_when_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book('Pipi', 2)
        self.assertEqual(f"Pipi has not enough copies to sell. Left: 1", str(error.exception))

    def test_sell_when_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = self.BOOKS
        result = self.bookstore.sell_book('RedHat', 2)
        self.assertEqual("Sold 2 copies of RedHat", result)
        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles['RedHat'])
        self.assertEqual(2, self.bookstore.total_sold_books)

    def test_string_works_properly(self):
        self.bookstore.availability_in_store_by_book_titles = {'RedHat': 2, 'Pipi': 1}
        self.bookstore.sell_book('RedHat', 1)
        result = str(self.bookstore)
        expected_result = f"Total sold books: 1\nCurrent availability: 2\n" \
                          f" - RedHat: 1 copies\n" \
                          f" - Pipi: 1 copies"
        self.assertEqual(expected_result, result)