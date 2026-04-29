from playwright.sync_api import Page
from utils.config import BASE_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def load_login(self):
        self.page.goto(f"{BASE_URL}/login")

    def enter_email(self, email: str):
        self.page.get_by_role("textbox").first.fill(email)

    def enter_password(self, password: str):
        self.page.locator("input[type='password']").fill(password)

    def click_forgot_password(self):
        self.page.get_by_role("link", name="Forgot password?").click()

    def click_continue(self):
        self.page.get_by_role("button", name="Continue", exact=True).click()