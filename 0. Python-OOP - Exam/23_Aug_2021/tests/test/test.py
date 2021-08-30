from unittest import TestCase, main

from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library('AI')

    def test_initialization(self):
        self.assertEqual('AI', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_property(self):
        self.library.name = 'Are'
        self.assertEqual('Are', self.library.name)

    def test_name_property_raise(self):
        expected = "Name cannot be empty string!"
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual(expected, str(ex.exception))

    def test_add_book(self):
        self.assertEqual({}, self.library.books_by_authors)
        self.library.add_book('AZ', 'Kniga')
        self.assertEqual({'AZ': ['Kniga']}, self.library.books_by_authors)

    def test_add_reader(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader('Pesho')
        self.assertEqual({'Pesho': []}, self.library.readers)

    def test_add_reader_msg(self):
        self.assertEqual({}, self.library.readers)
        self.library.add_reader('Pesho')
        self.assertEqual({'Pesho': []}, self.library.readers)
        expected = "Pesho is already registered in the AI library."
        result = self.library.add_reader('Pesho')
        self.assertEqual(expected, result)

    def test_rent_book_reader_not_there(self):
        expected = "Pesho is not registered in the AI Library."
        result = self.library.rent_book('Pesho', 'AZ', 'Kniga')
        self.assertEqual(expected, result)

    def test_rent_book_author_not_there(self):
        self.library.add_reader('Pesho')
        expected = "AI Library does not have any AZ's books."
        result = self.library.rent_book('Pesho', 'AZ', 'Kniga')
        self.assertEqual(expected, result)

    def test_rent_book_book_not_there(self):
        self.library.add_reader('Pesho')
        self.library.add_book('AZ', 'Kniga')
        expected = """AI Library does not have AZ's "Kniga2"."""
        result = self.library.rent_book('Pesho', 'AZ', 'Kniga2')
        self.assertEqual(expected, result)

    def test_rent_book_working(self):
        self.library.add_reader('Pesho')
        self.library.add_book('AZ', 'Kniga')
        self.assertEqual({'Pesho': []}, self.library.readers)
        self.assertEqual({'AZ': ['Kniga']}, self.library.books_by_authors)
        self.library.rent_book('Pesho', 'AZ', 'Kniga')
        self.assertEqual({'Pesho': [{'AZ': 'Kniga'}]}, self.library.readers)

    def test_rent_book_removing_book(self):
        self.library.add_reader('Pesho')
        self.library.add_book('AZ', 'Kniga')
        self.assertEqual({'Pesho': []}, self.library.readers)
        self.assertEqual({'AZ': ['Kniga']}, self.library.books_by_authors)
        self.library.rent_book('Pesho', 'AZ', 'Kniga')
        self.assertEqual({'Pesho': [{'AZ': 'Kniga'}]}, self.library.readers)
        self.assertEqual({'AZ': []}, self.library.books_by_authors)





