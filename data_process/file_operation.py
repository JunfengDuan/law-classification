from util.project import project
import pandas as pd


def read_csv(file_name, cols=None, dtype=None):
    data = pd.read_csv(project.data_dir+file_name, usecols=cols, dtype=dtype)
    data_list = data.values.tolist()
    return data_list


def read_file(file_name, encoding='utf-8'):
    with open(file_name, 'r', encoding=encoding) as f:
        return f.readlines()
