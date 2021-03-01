import time
from selenium.webdriver.common.by import By
from src.common.base import Base


class BaiduPage(Base):
    loc_search_input = (By.ID, 'kw')
    loc_search_button = (By.ID, 'su')
    loc_search_links = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def search_text(self, searchText):
        self.sendKeys(self.loc_search_input, searchText)
        self.click(self.loc_search_button)
        time.sleep(3)

    def getResult(self):
        # 获取当前的URL
        return self.find_elements(self.loc_search_links)
