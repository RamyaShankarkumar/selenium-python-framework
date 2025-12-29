import pytest
from pages.login_page import LoginPage
from utils.driver_factory import get_driver


def test_valid_login():
    driver = get_driver()
    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url
    assert driver.find_element("class name", "title").text == "Products"

    driver.quit()
