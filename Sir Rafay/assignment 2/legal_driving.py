def legal_driving(age):
    if age >= 16:
        return 'You are old enough to legally drive.'
    else:
        return 'You are not old enough to legally drive.'


def main():
    try:
        age = int(input("Enter your age: "))
    except Exception as e:
        return 'Age must be in numbers.'
    return legal_driving(age)


if __name__ == '__main__':
   print(main())