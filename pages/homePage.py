from selenium.webdriver.common.by import By
from utils.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_top_bar_dropdown_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.top_bar_dropdown_menu_css).click()

    def click_logout_menuitem(self):
        self.driver.find_element(By.CSS_SELECTOR, Locators.logout_css).click()

    def get_dashboard_breadcrumb(self):
        return self.driver.find_element(By.CSS_SELECTOR, Locators.dashboard_breadcrumb_css)

    def get_top_bar_dropdown_menu_items(self):
        return self.driver.find_elements(By.CSS_SELECTOR, Locators.top_bar_dropdown_menu_items_css)
