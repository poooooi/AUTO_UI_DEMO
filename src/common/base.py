class Base(object):
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout

    def get_driver(self):
        return self.driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    def find_elements(self, *args):
        return self.driver.find_elements(*args)

    def sendKeys(self, args, text=""):
        self.find_element(*args).send_keys(text)

    def click(self, args):
        self.find_element(*args).click()
