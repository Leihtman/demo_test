from page_objects import PageObject, PageElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.settings import get_settings

settings = get_settings()


class BasePage(PageObject):
    submit_button = PageElement(id_="submit")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.url = settings.base_url

    def open_page(self):
        self.browser.get(self.url)

    def send_keys(self, element, value):
        self.assert_element_found(element)
        assert element.is_enabled()
        assert element.is_displayed()
        element.send_keys(value)

    def click(self, element):
        self.assert_element_found(element)
        assert element.is_enabled()
        assert element.is_displayed()
        element.click()

    @staticmethod
    def assert_element_found(element):
        assert element is not None, "Element is not found on the page"

    def assert_element_displayed(self, locator_type: str, locator: str, timeout: int = 5):
        element_locator = (locator_type, locator)
        element = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(element_locator)
        )
        WebDriverWait(self.browser, timeout).until(
            EC.visibility_of(element)
        )
        assert element.is_displayed()

    def find_element_by_text(self, text: str):
        selector_type, value = PageElement(xpath=f"//*[contains(text(), '{text}')]").locator
        return self.browser.find_element(selector_type, value)

    def find_element_by_xpath(self, xpath_value: str):
        selector_type, value = PageElement(xpath=xpath_value).locator
        return self.browser.find_element(selector_type, value)

    def get_element_text_by_xpath(self, xpath_value):
        self.assert_element_displayed("xpath", xpath_value)
        result = self.find_element_by_xpath(xpath_value).text
        return result

    def get_text_and_assert_by_xpath(self, xpath_value, expected_value):
        result = self.get_element_text_by_xpath(xpath_value)
        assert result == expected_value
