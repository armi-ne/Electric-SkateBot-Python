# Take value, seperate values and convert

import string

mph_to_kph = 1.609344
kph_to_mph = 0.621371192

no_numb = str.maketrans(dict.fromkeys('0123456789'))
no_lett = str.maketrans(dict.fromkeys(string.ascii_lowercase))

print("The purpose of this code is to convert speed units")

def format_data(): # This will extract the value and unit from the input
    inputunit = str(value.translate(no_numb))
    inputspeed = str(value.translate(no_lett))
    return inputunit, inputspeed


def speed_converter(): # This will convert speed values interchangeably from mph to kph and vice versa
    inputunit, inputspeed = format_data()
    if inputunit == "kph" and desiredunit == "mph":
        print("Value: " + inputspeed + ", " + "oUnit: " + inputunit + ", " + "dUnit: " + desiredunit)
        print(str(int(float(inputspeed) * kph_to_mph)) + "mph")
    elif inputunit == "mph" and desiredunit == "kph":
        print("Value: " + inputspeed + ", " + "oUnit: " + inputunit + ", " + "dUnit: " + desiredunit)
        print(str(int(float(inputspeed) * mph_to_kph)) + "kph")
    else:
        print("Please input your values correctly")


while True: # This will get values
    try:
        value, to_, desiredunit = input('Input, e.g: 200mph to kph ').split()
        format_data()
        speed_converter()
    except ValueError:
        value, to_, desiredunit = input('Not valid data, try again! ').split()