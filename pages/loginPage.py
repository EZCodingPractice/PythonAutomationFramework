from selenium.webdriver.common.by import By
from utils.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, Locators.username_textbox_name).clear()
        self.driver.find_element(By.NAME, Locators.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, Locators.password_textbox_name).clear()
        self.driver.find_element(By.NAME, Locators.password_textbox_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.login_button_css).click()

    def get_login_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locators.login_title_css)
