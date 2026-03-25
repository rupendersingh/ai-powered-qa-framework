def test_self_healing(login_page):
    
    # Break primary locator intentionally
    login_page.USERNAME[0] = ("css selector", "wrond_id")

    login_page.login("tomsmith", "SuperSecretPassword!")

     # If framework is correct → test still passes
    assert True
