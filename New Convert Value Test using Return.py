"The purpose of this code is to convert speed units"
# Take value, seperate values and convert

import string

MPH_TO_KPH = 1.609344
KPH_TO_MPH = 0.621371192


def format_data(value):  # This will extract the value and unit from the input
    no_numb = str.maketrans(dict.fromkeys('0123456789'))
    no_lett = str.maketrans(dict.fromkeys(string.ascii_lowercase + string.punctuation))
    input_unit = value.translate(no_numb).split()[0]
    input_speed = float(value.translate(no_lett))
    return input_unit, input_speed


def speed_converter(unit, speed):  # This will convert speed values interchangeably from mph to kph and vice versa
    if 'k' in unit and ('m' in unit or 'p' in unit):
        output_unit = 'mph'
        print("Value: " + speed + ", " + "oUnit: " + unit + ", " + "dUnit: " + output_unit)
        print(str(speed * KPH_TO_MPH) + "mph")
    elif 'm' in unit and ('i' in unit or 'p' in unit):
        output_unit = 'kph'
        print("Value: " + speed + ", " + "oUnit: " + unit + ", " + "dUnit: " + output_unit)
        print(str(speed * MPH_TO_KPH) + "kph")


def get_value():  # This will get values
    while True:
        try:
            input = input('Input, e.g: 200mph to kph ').lower()
            return input
        except ValueError:
            print('Not valid data, try again!')


def main():
    input = get_value()
    unit, speed = format_data(input)
    speed_converter(unit, speed)
    

if __name__ == '__main__':
    getvalue()
