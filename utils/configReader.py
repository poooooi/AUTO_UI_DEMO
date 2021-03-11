"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等。
需在file_reader中添加相应的Reader进行处理。
"""
from utils.fileReader import YamlReader
from utils.fileReader import ExcelReader
from utils.utilConfig import CONFIG_FILE, DATA_PATH


class YamlConfig:
    def __init__(self):
        self.config = YamlReader(CONFIG_FILE).data

    def getYaml(self, yamlElement, index=0):
        """
        yaml是可以通过'---'分节的。
        用YamlReader读取返回的是一个list，第一项是默认的节，如果有多个节，可传入index来获取。
        这样我们其实可以把框架相关的配置放在默认节，其他的关于项目的配置放在其他节中。
        可以在框架中实现多个项目的测试。
        """
        return self.config[index].get(yamlElement)


class ExcelConfig:
    def __init__(self, filename, sheetname='Sheet1', title_line=True):
        # print(DATA_PATH+"\\"+filename + ":" + sheetname)
        self.excel = ExcelReader(DATA_PATH + "\\" + filename, sheetname,
                                 title_line).data

    def getExcel(self, index=0):
        return self.excel
