"""
日志类。通过读取配置文件，定义日志级别、日志文件名、日志格式等。
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.configReader import Config
from utils.utilConfig import LOG_PATH


class Logger(object):
    def __init__(self, logger_name='autoUIdemo'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)

        # 日志打印信息设定
        log_yml_info = Config().get('log')

        # 1. 日志名称
        # 若yaml文件中存在log配置且log下有file_name配置，则取该配置;否则使用‘test.log’作为文件名
        self.log_file_name = log_yml_info.get('file_name') if log_yml_info and log_yml_info.get('file_name') else 'test.log'

        # 2. 日志保留数量
        # 若yaml文件中存在log配置且log下有backup配置，则取该配置;否则使用默认配置5
        self.backup_count = log_yml_info.get('backup') if log_yml_info and log_yml_info.get('backup') else 5

        # 3. 日志输出级别
        self.console_output_level = log_yml_info.get('console_level') if log_yml_info and log_yml_info.get('console_level') else 'WARNING'
        self.file_output_level = log_yml_info.get('file_level') if log_yml_info and log_yml_info.get('file_level') else 'DEBUG'

        # 4. 日志输出格式
        get_formatter = log_yml_info.get('formatter') if log_yml_info and log_yml_info.get('formatter') else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(get_formatter)

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()