import string

MPH_TO_KPH = 1.609344
KPH_TO_MPH = 0.621371192


def format_data(value):  # This will extract the value and unit from the input
    input_unit = ''.join([i for i in value if not i.isdigit()]).split()[0]
    input_speed = float(''.join([i for i in value if not i.isalpha()]))
    return input_unit, input_speed


def speed_converter(unit, speed):  # This will convert speed values interchangeably from mph to kph and vice versa
    if 'k' in unit and ('m' in unit or 'p' in unit):
        output_unit = 'mph'
        unit = 'kph'
        print("Value: " + str(speed) + ", " + "oUnit: " + unit + ", " + "dUnit: " + output_unit)
        print(str(speed * KPH_TO_MPH) + "mph")
    elif 'm' in unit and ('i' in unit or 'p' in unit):
        output_unit = 'kph'
        unit = 'mph'
        print("Value: " + str(speed) + ", " + "oUnit: " + unit + ", " + "dUnit: " + output_unit)
        print(str(speed * MPH_TO_KPH) + "kph")


def get_value():  # This will get values
    # while True:
    user_input = input('Input, e.g: 200mph to kph\n> ').lower()
    return user_input


def main():
    user_input = get_value()
    unit, speed = format_data(user_input)
    speed_converter(unit, speed)

if __name__ == '__main__':
    main()
