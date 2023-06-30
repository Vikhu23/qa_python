import pytest


@pytest.fixture(scope='function')
def book_name():
    name = 'Война и мир'
    return name

@pytest.fixture(scope='function')
def book_rating():
    rating = 10
    return rating