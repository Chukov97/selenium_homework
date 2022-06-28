from selenium.webdriver.common.by import By

from .BasePage import BasePage


class ProductPage(BasePage):
    DESKTOP_BTN = (By.CSS_SELECTOR, "#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(1)")
    SHOW_ALL_BTN = (By.CSS_SELECTOR, "li.dropdown.open .see-all")
    PRODUCT_BTN = (
    By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(7) > div > div:nth-child(2) > div.caption > h4 > a")

    def open_page(self):
        self.driver.get(self.driver.url)
        self._find_element_and_click(self.DESKTOP_BTN)
        self._find_element_and_click(self.SHOW_ALL_BTN)
        self._find_element_and_click(self.PRODUCT_BTN)
