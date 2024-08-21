from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
import pytest
# import random
# from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    # chrome_driver.save_screenshot(f"{str(random.randint(100, 10000))}.png")


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)