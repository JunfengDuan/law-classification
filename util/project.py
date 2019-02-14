import os
import logging


class Project:
    def __init__(self, root_dir):
        self._root_dir = root_dir
        self._init_all_paths()

    def _init_all_paths(self):
        self._data_dir = os.path.join(self._root_dir, 'data')  # 数据目录
        self._log_dir = os.path.join(self._data_dir, 'log')  # 日志目录

    @property
    def root_dir(self):
        return self._root_dir + os.path.sep

    @property
    def data_dir(self):
        return self._data_dir + os.path.sep

    @property
    def log_dir(self):
        return self._log_dir + os.path.sep

    @staticmethod
    def init(root_dir):
        """
        :param root_dir:项目根目录
        :return:　返回项目操作的对象
        """
        pro = Project(root_dir)
        paths_to_create = [
            pro.data_dir,
            pro.log_dir
        ]
        for path in paths_to_create:
            if os.path.exists(path):
                continue
            else:
                os.makedirs(path)
        return pro

    def self_log(self):
        log_file = self.log_dir() + 'data.log'
        logger = logging.getLogger()
        logging.basicConfig(filename=log_file, format='%(asctime)s: %(levelname)s: %(message)s')
        logging.root.setLevel(level=logging.INFO)
        logger.info("Log file is %s", log_file)
        return logger


# 初始化整个项目的基础类
project = Project.init(os.path.dirname(os.path.dirname(__file__)))
