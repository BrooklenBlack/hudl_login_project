from utils.config import HUDL_EMAIL, HUDL_PASSWORD
from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_page_loads(page):
    login_page = LoginPage(page)
    login_page.load_login()
    assert "Log In" in page.title()

def test_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.load_login()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()
    login_page.enter_password(HUDL_PASSWORD)
    login_page.click_continue()

    assert "login" not in page.url.lower()

def test_login_with_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.load_login()

    login_page.enter_email("fakeemail@example.com")
    login_page.click_continue()

    login_page.enter_password("fakepassword")
    login_page.click_continue()

    expect(page.get_by_text("incorrect username or password")).to_be_visible()
    assert "login" in page.url.lower()

def test_empty_password(page):
    login_page = LoginPage(page)
    login_page.load_login()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    login_page.enter_password("")
    login_page.click_continue()

    expect(page.get_by_text("Please enter your password")).to_be_visible()
    assert "login" in page.url.lower()

def test_forgot_password_link(page):
    login_page = LoginPage(page)
    login_page.load_login()

    login_page.enter_email(HUDL_EMAIL)
    login_page.click_continue()

    login_page.click_forgot_password()
    login_page.click_continue()

    expect(page.get_by_role("heading", name="Check Your Email")).to_be_visible()


