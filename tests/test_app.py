import pytest

def pytest_runtest_setup():
    @test_app.route('/view_cart')
    def mock_view_cart():
        return "Mock cart view"

def test_homepage_loads(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'The Great Gatsby' in response.data

def test_empty_catalog(client, monkeypatch):
    monkeypatch.setattr('app.BOOKS', [])
    response = client.get('/')
    assert response.status_code == 200
    assert b'<div class="book-list">' not in response.data or b'No books' in response.data

def test_add_to_cart(client):
    response = client.post('/add_to_cart', data={'title': 'The Great Gatsby', 'quantity': '1'}, follow_redirects=True)
    print(f"Add response: {response.status_code}, {response.data}")
    assert response.status_code == 200
    assert b'Added' in response.data
    assert client.application.cart.get_items()[0].quantity == 1

def test_update_negative_quantity(client):
    client.post('/add_to_cart', data={'title': 'The Great Gatsby', 'quantity': '1'}, follow_redirects=True)
    response = client.post('/update_cart', data={'title': 'The Great Gatsby', 'quantity': '-1'}, follow_redirects=True)
    print(f"Update response: {response.status_code}, {response.data}")
    assert response.status_code == 200
    assert b'Removed' in response.data
    assert client.application.cart.is_empty()  #Bug 1 documentation

import timeit
import app

def test_get_total_price_performance(client):
    cart = client.application.cart
    cart.add_book(app.BOOKS[0], 1000)
    time = timeit.timeit(lambda: cart.get_total_price(), number=1000)
    print(f"Time for get_total_price: {time} seconds")
    assert time < 0.1

def test_get_total_price_profile(client):
    from app import cart
    cart.add_book(app.BOOKS[0], 1000)
