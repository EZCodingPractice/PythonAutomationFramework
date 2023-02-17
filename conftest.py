import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.service import Service

from utils import settings as read


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Read documentation")


@pytest.fixture(scope='class')
def test_setup(request):
    #  global driver
    chrome_service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    # firefox_service = Service(GeckoDriverManager().install())
    # firefox_options = Options()
    # chrome_options.add_argument('--headless')
    # firefox_options.add_argument('--headless')

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
    # elif browser == 'firefox':
    #     driver = webdriver.Firefox(service=firefox_service)

    driver.maximize_window()
    driver.get(read.baseURL)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print('Test Completed')
