from page_objects import PageObject
from config.settings import get_settings

settings = get_settings()


class BasePage(PageObject):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.url = settings.base_url

    def open_page(self):
        return self.browser.get(self.url)
