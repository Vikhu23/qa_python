from main import BooksCollector

import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_identical_books_one_book_added(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_rating()) != 2
    
    def test_set_rating_book_is_not_on_the_list_not_setting(self, book_rating):
    collector = BooksCollector()
    collector.set_book_rating('Горе от ума', book_rating)
    assert len(collector.get_books_rating()) != 10
    
    


        

