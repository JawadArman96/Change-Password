import change_password
from csv import reader


def load_data():
    result_data = []
    file = open("test_data.csv", "r", encoding='utf-8')
    data_lines = reader(file)
    for row in data_lines:
        if len(row) == 3:
            password = row[1]
            result = row[2]
        else:
            password = row[0]
            result = row[1]
        if result == "TRUE":
            bool_result = True
        else:
            bool_result = False
        row_data = [password, bool_result]
        result_data.append(row_data)
    return result_data


def test_change_password():
    result_data = load_data()
    for data in result_data:
        password = data[0]
        result = data[1]
        boolean_result = change_password.check_password(password)
        assert boolean_result == result
