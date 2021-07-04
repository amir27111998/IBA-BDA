# q1
def annual_investment(P, ratio, t):
    r = ratio / 100
    a = P*(1+(r*t))
    return 'After {} years at {}%, the investment will be worth ${}'.format(t, ratio, a)


def main():
    try:
        P = int(input('Enter the principal: '))
        ratio = float(input('Enter the rate of interest: '))
        years = int(input('Enter the number of years: '))
        return annual_investment(P, ratio, years)
    except Exception as e:
        print('Error: ', e)
        return 'Error When Converting Inputs'


if __name__ == '__main__':
    print(main())