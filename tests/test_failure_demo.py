def test_login_failure(driver):
    driver.get("https://example.com")

    # Intentional failure
    assert "Dashboard" in driver.title