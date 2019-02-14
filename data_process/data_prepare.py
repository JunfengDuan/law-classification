from data_process.pdbc import pdbc
from data_process.file_operation import read_csv


def gen_power_code_table():
    result = []

    data = read_csv('power_1.csv', ['种类', '职权种类'], {'种类': str})

    for line in data:
        id_type = list(map(str, line))
        if id_type not in result:
            result.append(id_type)
            print(id_type)

    result_sql = 'insert into power_code_table values (%s,%s)'
    pdbc.save(result_sql, result)


if __name__ == '__main__':
    gen_power_code_table()
