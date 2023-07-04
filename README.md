# Финальный проект qa_python_sprint_2
 Проект по написанию unit тестов к `class BooksCollector:`
    В проекте была использована библиотека `pytest`, декораторы `pytest.mark.parametrzie` `pytest.fixture`

Фикстуры `book_name` и `book_rating` использованы с целью удобства использования тестовых данных для позитивных проверок.

# Тесты
1. Тест метода добавления книги
 
В  тесте методом добавления книг, добавляются две книги, проверяем возможность добавления нескольких книг сразу 
```python 
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2
   ```
ОР:Книги добавляютсz


2. Тест метода добавления книги

В тесте методом добавляется одинаковая книга дважды, с целью проверки создания дубля
```python
    def test_add_new_book_identical_books_one_book_added(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_rating()) == 1
```
ОР:*Книга не дублируется*


3. Тест метода добавления рейтинга для книги

В тесте,методом устанавливления рейтинга, устанавливается рейтинг не добавленной книги в список книг
```python
    def test_set_rating_book_is_not_on_the_list_not_setting(self, book_rating):
        collector = BooksCollector()
        collector.set_book_rating('Горе от ума', book_rating)
        assert collector.get_book_rating('Горе от ума') == None
```
ОР:*Рейтинг не устанавливается*


4. Тест метода установления рейтинга 

Тестом устанавливается рейтинг 0,-1,11, методом установления рейтинга книгам, за пределами установленными `class BooksCollector:`(1-10) 
В тесте 3 проверки, на негативные значения, через `pytest.mark.parametrize`
```python
@pytest.mark.parametrize(
        'rating',[-1,11,0]
        )
    def test_set_rating_book_less_than_1_or_set_rating_book_more_than_10_not_setting(self, book_name,rating):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)
        assert collector.get_book_rating(book_name) == 1
```
ОР:Рейтинг устанавливается по умолчанию(1)


5. Тест метода добавления книги

Тест проверяет метод `self.books_rating[name] = 1`(установление рейтинга по умолчанию)
```python     
   def test_added_book_has_no_rating_setting_rating_by_default(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert collector.get_book_rating(book_name) != 0
```
ОР: Рейтинг устанавливается

6. Тест метода добавления книги в список избранного

Тестом добавляется книга в список избранного 
```python
 def test_add_book_in_list_of_favorites_books_book_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()
```
ОР: Книга добавляется в список избранного

7. Тест метода удаления книги из списка избранного

Тест  удаляет книгу добавленную в список избранного
```python
    def test_delete_book_in_list_of_favorites_books_book_deleted(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()
```

ОР:Книга удаляется

8. Тест метода добавления книги в список избранного

Тест использует метод добавления книги в список избранного, без добавления книги в `self.books_rating = {}` 
```python
    def test_cannot_add_a_book_to_list_of_favorites_books_if_it_is_not_in_the_books_rating_book_not_added(self, book_name):
        collector = BooksCollector()
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 0
```

ОР:Книга не добавляется

9. Тест метода вывода книги по указанному рейтингу

В тестt с помощью `pytest.mark.parametrize`добавляется несколько книги с разным рейтингом, для проверки вызова метода по рейтингу `def get_books_with_specific_rating(self, rating):`
```python
 def test_get_book_with_specific_rating_book_gets(self, books, rating):
        collector = BooksCollector()
        collector.add_new_book(books)
        collector.set_book_rating(books, rating)
        assert books in collector.get_books_with_specific_rating(rating)
```
ОР:Метод вызывает книги исходя из указанного рейтинга
