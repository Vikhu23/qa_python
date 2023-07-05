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
        assert len(collector.get_books_rating()) == 1
    
    def test_set_rating_book_is_not_on_the_list_not_setting(self, book_rating):
        collector = BooksCollector()
        collector.set_book_rating('Горе от ума', book_rating)
        assert collector.get_book_rating('Горе от ума') is None
    
    
    @pytest.mark.parametrize(
        'rating',[-1,11,0]
    )
    def test_set_rating_book_less_than_1_or_set_rating_book_more_than_10_not_setting(self, book_name,rating):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)
        assert collector.get_book_rating(book_name) == 1
    
    def test_added_book_has_no_rating_setting_rating_by_default(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_rating(book_name) == 1
    
    def test_add_book_in_list_of_favorites_books_book_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
        
    
    def test_delete_book_in_list_of_favorites_books_book_deleted(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()
        
    
    def test_cannot_add_a_book_to_list_of_favorites_books_if_it_is_not_in_the_books_rating_book_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0
    
    @pytest.mark.parametrize(
        'books , rating',
        [
            ['Горе от ума', 9],
            ['Фауст', 8],
            ['Мертвые души', 5]
        ]
    )
    def test_get_book_with_specific_rating_book_gets(self, books, rating):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_rating(books, rating)
        assert books in collector.get_books_with_specific_rating(rating)
        