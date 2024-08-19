from selenium.webdriver.common.by import By
from pages.base_page import BasePage


header_title_loc = (By.TAG_NAME, "h1")


class SalePage(BasePage):

    page_url = "/sale.html"

    # def open_page(self):
    #     self.driver.get("https://magento.softwaretestingboard.com/sale.html")

    def check_header_tittle_is(self, text):
        header_tittle = self.find(header_title_loc)
        assert header_tittle.text == text
