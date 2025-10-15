# conftest.py
import pytest
import app
from models import Cart
from flask import Flask

test_app = app.app
test_app.config.update(
    TESTING=True,
    WTF_CSRF_ENABLED=False,
    SERVER_NAME='localhost',
    DEBUG=True
)

@pytest.fixture(scope='function')
def client():
    if not hasattr(test_app, 'cart') or test_app.cart is None:
        test_app.cart = Cart()
    with test_app.test_client() as client:
        with client.session_transaction() as session:
            session['user_email'] = 'demo@bookstore.com'
            client.application.cart.clear()
        client.application.config['APPLICATION_ROOT'] = '/'
        yield client