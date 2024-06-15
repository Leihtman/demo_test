import allure
from page_objects import PageObject, PageElement
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

    @staticmethod
    def assert_element_found(element):
        assert element is not None, "Element is not found on the page"

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

    def find_element_by_text(self, text: str):
        selector_type, value = PageElement(xpath=f"//*[contains(text(), '{text}')]").locator
        return self.browser.find_element(selector_type, value)

    def find_element_by_xpath(self, xpath_value: str):
        selector_type, value = PageElement(xpath=xpath_value).locator
        return self.browser.find_element(selector_type, value)
