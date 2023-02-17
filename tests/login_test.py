import pytest
import allure
import time
import moment
from hamcrest import assert_that, equal_to
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import settings as read
from utils import commons as utils


@pytest.mark.usefixtures('test_setup')
class TestLogin:

    def test_page_title(self):
        driver = self.driver
        print(f'The page title is {driver.title}')
        actual_page_title = driver.title
        expected_page_title = "OrangeHRM"
        assert_that(actual_page_title, equal_to(expected_page_title),
                    f'{actual_page_title} is not the expected title.')

    def test_login(self):
        driver = self.driver

        try:
            login = LoginPage(driver)
            login.enter_username(read.USERNAME)
            login.enter_password(read.PASSWORD)
            login.click_login_button()
            time.sleep(1)
            assert driver.title == 'OrangeHRM'

        except AssertionError as error:
            print('Assertion error occurred')
            print(error)
            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + current_time
            allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)

            screenshots_dir = utils.get_screenshot_dir()
            driver.get_screenshot_as_file(screenshots_dir + screenshot_name + '.png')
            raise
        except:
            print('There was an exception')
            raise
        else:
            print('No exceptions occurred')
        finally:
            print('I am inside the finally block..')

    def test_dashboard_breadcrumb(self, test_setup):
        driver = self.driver
        homepage = HomePage(driver)
        dashboard_breadcrumb = homepage.get_dashboard_breadcrumb()
        actual_dashboard_breadcrumb = dashboard_breadcrumb.get_attribute('innerHTML')
        expected_dashboard_breadcrumb = "Dashboard"
        print(f'The UI dashboard breadcrumb is {actual_dashboard_breadcrumb}')
        assert_that(actual_dashboard_breadcrumb, equal_to(expected_dashboard_breadcrumb),
                    f'{actual_dashboard_breadcrumb} is not the expected breadcrumb.')

    def test_top_nav_dropdown_menu_items(self, test_setup):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_top_bar_dropdown_menu()
        menu_items = homepage.get_top_bar_dropdown_menu_items()
        ui_menu_items = []
        expected_menu_items = ['About', 'Support', 'Change Password', 'Logout']

        for item in menu_items:
            ui_menu_items.append(item.get_attribute('innerHTML'))

        print(f'The UI menu items are {ui_menu_items}')
        assert_that(ui_menu_items, equal_to(expected_menu_items),
                    f'{ui_menu_items} are not the expected menu items.')

        homepage.click_logout_menuitem()

        login = LoginPage(driver)
        print(f'The page title is {driver.title}')
        login_title = login.get_login_title()
        actual_login_title = login_title.get_attribute('innerHTML')
        expected_login_title = "Login"
        assert_that(actual_login_title, equal_to(expected_login_title),
                    f'{actual_login_title} is not the expected title.')
