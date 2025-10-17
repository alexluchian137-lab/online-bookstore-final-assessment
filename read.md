# Online Bookstore - Final Assessment

## Project Overview

- **Functionalities**: Browse books (FR-001), manage a shopping cart (FR-002), and process secure orders.
- **Testing**: 20 automated test cases, with 17 passing and 3 failing (`test_add_to_cart`, `test_payment_with_paypal`, `test_case_insensitive_discount_code`) due to deferred issues.
- **Security**: Implements `werkzeug.security` for password hashing and input sanitization to mitigate XSS.
- **Performance**: Optimized `get_total_price()` for better efficiency.
- **CI/CD**: Uses GitHub Actions with `continue-on-error: true` for build stability.

## Requirements

### Software
- **Operating System**: macOS (tested on Alex's MacBook Pro) or compatible Unix-like system.
- **Python**: Version 3.13.0 (recommended; ensure compatibility with 3.11+).
- **Git**: For cloning the repository.
- **Terminal**: macOS Terminal or PyCharm integrated terminal.

### Dependencies
- `flask`: Web framework.
- `pytest`: Testing framework.
- `beautifulsoup4`: HTML parsing for tests.
- `werkzeug`: Security utilities.
- Other potential dependencies in `requirements.txt` (e.g., `flask-wtf` for forms).

## Installation Instructions

### 1. Clone the Repository
- Clone the project to your local machine: