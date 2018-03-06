# Converter Functions

import string

# Converter Functions


def executer(a, b, c):  # This is the main executer Function in which all the different functions are called upon and returned answers will be input into the next one e.t.c
    ov, ou, du = a, b, c
    formatted_speed, formatted_unit, desired_un = data_formatter(ov, ou, du)
    printthis = str(speed_converter(formatted_speed, formatted_unit, desired_un))
    return printthis


def data_formatter(value, unit, dunit):  # The purpose of this function is to take the user input and seperate the words and numbers, then assign them to new variables and return them
    no_numb = str.maketrans(dict.fromkeys('0123456789'))
    no_lett = str.maketrans(dict.fromkeys(string.ascii_lowercase))
    user_speed = float(value)
    user_unit = unit.translate(no_numb)
    desired = dunit
    return user_speed, user_unit, desired


def speed_converter(a, b, c):  # This is the final step, the formatted unit and speed are taken in and through an IF statement it will find out the desired unit and will then proceed to convert it, printing out the result.
    # Conversion Dictionary
    conversion = {"mph_kph": 1.60934, "kph_mph": 0.621371, "km_mi": 0.621371,
"mi_km": 1.60934, "Wh_km": 0.1, "Wh_mi": 0.0621371, "cm_inch": 0.393701, "inch_cm": 2.54}
    # KPH to MPH
    if b == "kph" and c == "mph":
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(int(float(a) * conversion["kph_mph"])) + c
    # MPH to KPH
    elif b == "mph" and c == "kph":
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(int(float(a) * conversion["mph_kph"])) + c
    # KM to MI
    elif (b == "km" or b == "kilometers" or b == "kilometres" or b == "kilometer" or b == "kilometre") and (c == "mi" or c == "miles" or c == "mile"):
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["km_mi"]) + c
    # MI to KM
    elif (b == "mi" or b == "miles" or b == "mile") and (c == "km" or c == "kilometers" or c == "kilmetres" or c == "kilometer" or c == "kilometre"):
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["mi_km"]) + c
    # Wh
    elif b == "wh":
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = str(a) + "wh should get you: {0:.2f}".format(float(a) * conversion["Wh_mi"]) + " miles, or {0:.2f}".format(float(a) * conversion["Wh_km"]) + " kilometers. Please note that this is an ESTIMATED value."
    # Inch to CM
    elif (b == "inch" or b == "in") and (c == "cm" or c == "centimeters" or c == "centimetres" or c == "centimeter" or c == "centimetre"):
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["inch_cm"]) + " cm"
    # CM to Inch
    elif (b == "cm" or b == "centimeters" or b == "centimetres" or b == "centimeter" or b == "centimetre") and (c == "inch" or c == "in"):
        print("Value: " + str(a) + ", " + "Original Unit: " + b + ", " + "Desired Unit: " + c)
        result = "{0:.2f}".format(float(a) * conversion["cm_inch"]) + " inches"
    # Bad Input
    else:
        result = "Please input your values correctly"
    return result
