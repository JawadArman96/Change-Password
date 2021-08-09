import change_password
from csv import reader


def load_data(file_name):
    result_data = []
    file = open(file_name, "r", encoding='utf-8')
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


def load_data_old_pw(file_name):
    result_data = []
    file = open(file_name, "r", encoding='utf-8')
    data_lines = reader(file)
    for row in data_lines:
        if len(row) == 4:
            old_password = row[1]
            new_password = row[2]
            result = row[3]
        else:
            old_password = row[0]
            new_password = row[1]
            result = row[2]
        if result == "TRUE":
            bool_result = True
        else:
            bool_result = False
        row_data = [old_password, new_password, bool_result]
        result_data.append(row_data)
    return result_data


def test_check_password():
    result_data = load_data("test_data.csv")
    for data in result_data:
        password = data[0]
        actual_result = data[1]
        result = change_password.check_password(password)
        if actual_result != result:
            print("TEST:: "+password + " actual result: " + str(actual_result) + " output result: " + str(result))
        assert actual_result == result


def test_change_password():
    result_data = load_data_old_pw("test_data_old_pw.csv")
    defined_old_pw = ""
    for data in result_data:
        old_password = data[0]
        new_password = data[1]
        actual_result = data[2]
        defined_old_pw = old_password
        result = change_password.change_password(old_password, new_password)
        if actual_result != result:
            print("TEST:: " + old_password + "->" + new_password + " actual result: "
                  + str(actual_result) + " output result: " + str(result))
        assert actual_result == result
    result_data = load_data("test_data.csv")
    for data in result_data:
        new_password = data[0]
        actual_result = data[1]
        result = change_password.change_password(defined_old_pw, new_password)
        if actual_result != result:
            print("TEST:: " + defined_old_pw + "->" + new_password + " actual result: "
                  + str(actual_result) + " output result: " + str(result))
        assert actual_result == result
