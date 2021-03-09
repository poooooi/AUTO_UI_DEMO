from selenium.common.exceptions import NoSuchElementException


class Base(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout

    def get_driver(self):
        return self.driver

    def find_element(self, args):
        return self.driver.find_element(*args)

    def find_elements(self, args):
        return self.driver.find_elements(*args)

    def sendKeys(self, args, text=""):
        self.find_element(args).send_keys(text)

    def click(self, args):
        self.find_element(args).click()

    def clear(self, args):
        self.find_element(args).clear()

    def getText(self, args):
        return self.find_element(args).text

    def refresh(self):
        self.driver.refresh()

    def getAttribute_style(self, args):
        return self.find_element(args).get_attribute('style')

    def ElementExist(self, args):
        try:
            self.find_element(args)
            return True
        except NoSuchElementException:
            return False
