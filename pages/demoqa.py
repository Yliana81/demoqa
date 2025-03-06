from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver,'#app > header > a')
        self.btn_elements = WebElement(driver,'#app > div > div > div.home-body > div > div:nth-child(1)')
        # элемент footer
        self.footer = WebElement(driver, '#app > footer > span')
        # элемент с текстом 'Please select an item from left to start practice.'
        self.center  = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')

    def exist_icon(self):
        try:
            self.icon.find_element()
        except NoSuchElementException:
            return False
        return True