import pytest


@pytest.fixture()
def book_name():
    name = 'Война и мир'
    return name

@pytest.fixture()
def book_rating():
    rating = 10
    return rating