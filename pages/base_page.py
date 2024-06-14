from page_objects import PageObject, PageElement
from config.settings import get_settings

settings = get_settings()


class BasePage(PageObject):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.url = settings.base_url

    def open_page(self):
        return self.browser.get(self.url)

    def get_element_by_text(self, text: str):
        selector_type, value = PageElement(xpath=f"//*[contains(text(), '{text}')]").locator
        return self.browser.find_element(selector_type, value)
