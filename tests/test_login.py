def test_login_page_loads(page):
    page.goto("https://www.hudl.com/login")
    assert "Log In" in page.title()