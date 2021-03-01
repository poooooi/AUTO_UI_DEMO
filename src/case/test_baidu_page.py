import os
import ddt
import time
import unittest

from selenium import webdriver
from utils.utilConfig import DRIVER_PATH
from utils.configReader import YamlConfig, ExcelConfig
from utils.log import logger
from src.page.baidu_page import BaiduPage

excelData = ExcelConfig("searchText.xls", "搜索内容").getExcel()


@ddt.ddt
class WebTest(unittest.TestCase):
    URL = YamlConfig().getYaml('URL')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=os.path.join(DRIVER_PATH, 'chromedriver.exe'))
        cls.driver.maximize_window()
        cls.baidupage = BaiduPage(cls.driver)

    def setUp(self):
        self.driver.get(self.URL)
        time.sleep(2)

    @ddt.data(*excelData)
    def test_search(self, data):
        '''搜索的case'''
        # 1.打开浏览器;
        # 2.找到搜索框，输入"python";
        # 3.点击"搜索"按钮;
        # 4.抓取当前页面中所有结果的标题并输出

        self.baidupage.search_text(data)
        links = self.baidupage.getResult()  # 获取当前的URL
        for link in links:
            logger.info(link.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
