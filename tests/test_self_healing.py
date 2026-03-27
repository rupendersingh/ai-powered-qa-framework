def test_self_healing(login_page):

    # Override ENTIRE locator list (correct way)
    login_page.USERNAME = [
        ("css selector", "#wrong-id"),
        ("xpath", "//input[@id='username']")
    ]

    login_page.login("tomsmith", "SuperSecretPassword!")

    assert True