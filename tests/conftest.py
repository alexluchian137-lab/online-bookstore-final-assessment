import pytest
from flask import Flask
import os
import app  # Import the module


test_app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'))
test_app.secret_key = 'test-key'
test_app.config.update(
    TESTING=True,
    WTF_CSRF_ENABLED=False
)

from app import cart, BOOKS, users, orders
test_app.cart = cart
test_app.BOOKS = BOOKS
test_app.users = users
test_app.orders = orders


def register_routes(app_instance):
    @app_instance.route('/')
    def index():

        return app.index()

    @app_instance.route('/add_to_cart', methods=['POST'])
    def add_to_cart():
        return app.add_to_cart()

    @app_instance.route('/update_cart', methods=['POST'])
    def update_cart():
        return app.update_cart()

    @app_instance.route('/view_cart')
    def view_cart():

        return app.view_cart()

register_routes(test_app)

@pytest.fixture
def client():
    with test_app.test_client() as client:
        with client.session_transaction() as session:
            session['user_email'] = 'demo@bookstore.com'
            test_app.cart.clear()
        with test_app.app_context():
            print(f"Test app routes: {[rule.rule for rule in test_app.url_map.iter_rules()]}")
        yield client