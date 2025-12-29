from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def login(self, user, pwd):
        self.driver.find_element(*self.USERNAME).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.LOGIN_BTN).click()

        # Wait for inventory page
        self.wait.until(EC.visibility_of_element_located(self.TITLE))
