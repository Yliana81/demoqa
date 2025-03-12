from components.components import WebElement
from pages.base_page import BasePage

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_content = WebElement(driver, '#section1Content > p')
        self.section_heading = WebElement(driver, '#section1Heading')
        self.content_elem_first = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.content_elem_second = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.content_elem_third = WebElement(driver, '#section3Content > p')

