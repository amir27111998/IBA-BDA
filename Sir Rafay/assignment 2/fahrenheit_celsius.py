def f_to_c(temp):
    return (temp - 32) * 5/9


def c_to_f(temp):
    return (temp * (9 / 5)) + 32


def calculate(choice):
    choice = choice.lower()
    available_conversions = {
        'f': {'inp_in': 'Celsius', 'converter': c_to_f},
        'c': {'inp_in': 'Fahrenheit', 'converter': f_to_c}
    }
    if ord(choice) != ord('c') and ord(choice) != ord('f'):
        return "Conversion Not Available."
    else:
        try:
            temp = float(input(f'Your choice {choice.upper()}\n'
                               f'Please enter the temperature in {available_conversions[choice]["inp_in"]}: '))
            return round(available_conversions[choice]["converter"](temp),2)
        except Exception:
            return "Temperature should be number. "


def main():
    choice = input('Press C to convert from Fahrenheit to Celsius \n'
                   'Press F to convert from Celsius to Fahrenheit \n')
    return calculate(choice)


if __name__ == '__main__':
    print(main())