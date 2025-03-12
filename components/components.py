from selenium.webdriver.common.by import By

class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # в классе компонентов создайте метод для получения текста с элементов get_text(self).
    # текст из элемента считывайте так str(self.find_element().text)
    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

