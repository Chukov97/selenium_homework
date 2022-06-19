from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = driver.logger

    def open_page(self):
        self.logger.info(f"Opening url {self.driver.url}")
        with allure.step(f"Открывается страница {self.driver.url}"):
            self.driver.get(self.driver.url)

    def _verify_element_visibility(self, locator, time=3):
        self.logger.info(f"Check if element {locator} is present")
        with allure.step(f"Элемент {locator} присутствует на странице и виден юзеру"):
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator: {locator}")

    def _verify_elements_presence(self, locator, time=3):
        self.logger.info(f"Check if element {locator} is present")
        with allure.step(f"Элементы {locator} присутствуют на странице"):
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator: {locator}")

    def _verify_elements_visibility(self, locator, time=3):
        self.logger.info(f"Check if elements {locator} are present")
        with allure.step(f"Элементы {locator} присутствуют на странице и видны юзеру"):
            return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator: {locator}")

    @allure.step("Клик по элементу на странице")
    def _find_element_and_click(self, locator):
        self.logger.info(f"Check if element {locator} is present and click")
        element = self._verify_element_visibility(locator)
        element.click()

    def _fill_input_field(self, field, text):
        self.logger.info(f"Input {text} in input {field}")
        with allure.step(f"Ввод значения {text} в поле {field}"):
            field = self._verify_element_visibility(field)
            field.click()
            field.clear()
            field.send_keys(text)
