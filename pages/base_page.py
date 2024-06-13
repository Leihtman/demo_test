from page_objects import PageObject
from config.settings import get_settings

settings = get_settings()


class BasePage(PageObject):

    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.webdriver = webdriver
        self.url = settings.base_url

    def open_page(self):
        return self.webdriver.get(self.url)
