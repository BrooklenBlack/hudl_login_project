from utils.config import HUDL_EMAIL, HUDL_PASSWORD, BASE_URL
from playwright.sync_api import expect

def test_login_page_loads(page):
    page.goto(f"{BASE_URL}/login")
    assert "Log In" in page.title()

def test_login_with_valid_credentials(page):
    page.goto(f"{BASE_URL}/login")

    page.get_by_role("textbox").first.fill(HUDL_EMAIL)
    page.get_by_role("button", name="Continue", exact=True).click()

    page.locator("input[type='password']").fill(HUDL_PASSWORD)
    page.get_by_role("button", name="Continue", exact=True).click()

    assert "login" not in page.url.lower()

def test_login_with_invalid_credentials(page):
    page.goto(f"{BASE_URL}/login")

    page.get_by_role("textbox").first.fill("invalid@example.com")
    page.get_by_role("button", name="Continue", exact=True).click()

    page.locator("input[type='password']").fill("invalidpassword")
    page.get_by_role("button", name="Continue", exact=True).click()

    expect(page.get_by_text("email or password is incorrect")).to_be_visible()
    assert "login" in page.url.lower()

def test_empty_password(page):
    page.goto(f"{BASE_URL}/login")

    page.get_by_role("textbox").first.fill(HUDL_EMAIL)
    page.get_by_role("button", name="Continue", exact=True).click()

    page.locator("input[type='password']").fill("")
    page.get_by_role("button", name="Continue", exact=True).click()

    expect(page.get_by_text("Please enter your password")).to_be_visible()
    assert "login" in page.url.lower()