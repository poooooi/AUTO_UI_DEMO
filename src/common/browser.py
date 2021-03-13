'''
做了简单封装，可根据传入的参数选择浏览器的driver去打开对应的浏览器。
并且加了一个保存截图的方法，可以保存png截图到report目录下。
'''

import time
import os
from selenium import webdriver
from utils.utilConfig import DRIVER_PATH, REPORT_PATH

CHROMEDRIVER_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')
IEDRIVER_PATH = os.path.join(DRIVER_PATH, 'IEDriverServer.exe')
PHANTOMJSDRIVER_PATH = os.path.join(DRIVER_PATH, 'phantomjs.exe')

TYPES = {
    'firefox': webdriver.Firefox,
    'chrome': webdriver.Chrome,
    'ie': webdriver.Ie,
    'phantomjs': webdriver.PhantomJS
    }

EXECUTABLE_PATH = {
    'firefox': 'wires',
    'chrome': CHROMEDRIVER_PATH,
    'ie': IEDRIVER_PATH,
    'phantomjs': PHANTOMJSDRIVER_PATH
    }


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        if (self.browser == "chrome"):
            option = webdriver.ChromeOptions()
            # 无头浏览器，执行时隐藏窗口
            # option.add_argument('headless')
            # 防止打印一些无用的日志
            option.add_experimental_option("excludeSwitches",
                                        ['enable-automation', 'enable-logging'])
            self.driver = webdriver.Chrome(chrome_options=option, executable_path=CHROMEDRIVER_PATH)
        else:
            self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self.driver

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\\' + 'screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot_path_name = screenshot_path + '\\%s_%s.png' % (name, tm)
        screenshot = self.driver.save_screenshot(screenshot_path_name)
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
