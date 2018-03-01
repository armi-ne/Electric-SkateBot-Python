# My new attempt after doing 48% of the codecademy course, based on Test v2.py and inspired by Jinra's Version
import string

mph_to_kph = 1.609344
kph_to_mph = 0.621371192

no_numb = str.maketrans(dict.fromkeys('0123456789'))
no_lett = str.maketrans(dict.fromkeys(string.ascii_lowercase))


def user_input():
    user_input = input("Please input your desired conversion, e.g. 200mph ").lower()
    return user_input


def data_formatter(arg):
    user_speed = arg.translate(no_lett)
    user_unit = arg.translate(no_numb)
    return user_speed, user_unit


def speed_converter(a, b):
    if b == "kph":
        desired_unit = "mph"
        print("Value: " + a + ", " + "oUnit: " + b + ", " + "dUnit: " + desired_unit)
        print(str(int(float(a) * kph_to_mph)) + "mph")
    elif b == "mph":
        desired_unit = "kph"
        print("Value: " + a + ", " + "oUnit: " + b + ", " + "dUnit: " + desired_unit)
        print(str(int(float(a) * mph_to_kph)) + "kph")
    else:
        print("Please input your values correctly")


def executer():
    original = user_input()
    formatted_speed, formatted_unit = data_formatter(original)
    speed_converter(formatted_speed, formatted_unit)

executer()
