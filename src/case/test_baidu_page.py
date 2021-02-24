import time
import unittest

from selenium import webdriver
from utils.utilConfig import DRIVER_PATH
from utils.configReader import Config
from utils.log import logger

class LoginTest(unittest.TestCase):
    URL = Config().get('URL')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')

    def setUp(self):
        self.driver.get(self.URL)
        time.sleep(2)


    def test_search(self):
        '''搜索的case'''
        # 1.打开浏览器;
        # 2.找到搜索框，输入"paython";
        # 3.点击"搜索"按钮;
        # 4.抓取当前页面中所有结果的标题并输出
        self.driver.find_element_by_xpath("//input[@id='kw']").send_keys("python自动化")
        self.driver.find_element_by_xpath("//input[@id='su']").click()
        time.sleep(3)

        #获取当前的URL
        links = self.driver.find_elements_by_xpath(".//div[contains(@class, \"result\")]/h3/a")
        for link in links:
            logger.info(link.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()   # 编辑器问题

if __name__ == "__main__":
    unittest.main()