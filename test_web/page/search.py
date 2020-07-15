import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


class Search:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def search_by(self, author=None, keyword=None):
        if keyword is not None:
            search_input=self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
            search_input.clear()
            search_input.send_keys(keyword)
            # search_input.send_keys(Keys.ENTER)

        if author is not None:
            self.driver.find_element(By.NAME, 'user-selector-renamed').send_keys(author)
            self.driver.find_element(By.CSS_SELECTOR, 'li .selected').click()

        self.driver.save_screenshot("/tmp/1.png")
        allure.attach.file('/tmp/1.png', attachment_type=allure.attachment_type.PNG)
        self.driver.find_element(By.CSS_SELECTOR, 'button.search-cta').click()
        self.driver.save_screenshot("/tmp/2.png")
        allure.attach.file('/tmp/2.png', attachment_type=allure.attachment_type.PNG)

        return self

    def get_results(self):
        return [element.text for element in self.driver.find_elements(By.CSS_SELECTOR, 'div.fps-topic')]

    def get_authors(self):
        return [element.get_attribute('data-user-card') for element in
                self.driver.find_elements(By.CSS_SELECTOR, 'div.fps-result .author a')]
