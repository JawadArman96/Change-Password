import re
from Levenshtein import distance
from flask import Flask
app = Flask(__name__)


saved_password = "abcdefgABCDEFG012345*"
error_message = ""


@app.route("/get-password", methods=['GET'])
def get():
    return "old password: " + saved_password


@app.route("/set-password/<string:password>", methods=['POST'])
def set_password(password):
    message = request_set(password)
    return message


@app.route("/change-password/<string:password>", methods=['POST'])
def change_password_api(password):
    message = request_change(password)
    return message


def change_password(old_password, new_password):
    global error_message
    # ###### Checking with previous password ############
    if new_password == old_password:  # checking if password
        error_message = "Password matched with the old one"  # is equal
        return False
    # checking if 80% match with previous
    dist = distance(old_password, new_password)
    max_len = max(len(old_password), len(new_password))
    percentage = (1 - (dist/max_len)) * 100
    # print(str(dist) + " " + str(max_len) + " " + str(percentage))
    if percentage >= 80:
        error_message = "password matches 80% with the old one"
        return False
    #############################################
    # check password with the requirement
    return check_password(new_password)


def check_password(password):
    global error_message
    special_chars = ['!', '@', '#', '$', '&', '*']
    # define regex (in total min length of the password should be 19)
    reg_ex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$&*])[A-Za-z0-9!@#$&*]{19,}$"
    # compiling regex
    pattern = re.compile(reg_ex)
    # searching regex
    match = re.search(pattern, password)
    # validating conditions
    if not match:  # checking alphanumeric,digits,
        error_message = "should be 18 alphanumeric characters, atleast " \
                        "1 uppercase, atleast 1 lowercase, 1 special characters"
        return False  # special characters and length
    # checking repetition
    numeric_count = 0
    for i in range(0, 26):  # repeating alphabet
        char_val = chr(ord('a') + i)  # checking lowercase repeat
        count_val = password.count(char_val)
        if count_val > 4:
            error_message = "Repeated lowercase 4 times"
            return False
        char_val = chr(ord('A') + i)
        count_val = password.count(char_val)  # checking uppercase repeat
        if count_val > 4:
            error_message = "Repeated uppercase 4 times"
            return False
        if i < 10:
            char_val = chr(ord('0') + i)
            count_val = password.count(char_val)  # repeating numeric
            numeric_count += count_val
            if count_val > 4:
                error_message = "Repeated numbers 4 times"
                return False

    # checking extra special characters
    count_val = 0
    for char_val in special_chars:
        count_val += password.count(char_val)
    if count_val > 4:
        error_message = "More than 4 special characters"
        return False
    # checking if 50% is a number
    percentage = (numeric_count / len(password)) * 100
    if percentage >= 50:
        error_message = "50% of the password should not be number"
        return False
    return True


def request_change(req_password):
    global saved_password
    bool_val = change_password(saved_password, req_password)
    if bool_val:
        saved_password = req_password
        message = "Password change successfully"
    else:
        message = error_message
    return message


def request_set(req_password):
    global saved_password
    bool_val = check_password(req_password)
    if bool_val:
        saved_password = req_password
        message = "Password set successfully"
    else:
        message = error_message
    return message


if __name__ == "__main__":
    app.run(debug=True)
    # print(change_password(saved_password, sys.argv[1]))
