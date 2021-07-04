def tax_calc(amount, state):
    tax = 0
    total = ''
    if state == 'WI':
        tax = 5.5 / 100
        total += f'The subtotal is ${amount}. \n'
        total += f'The tax is ${tax}. \n'
    total += f'The total is: ${amount+tax}'
    return total


def main():
    try:
        amount = float(input('What is the order amount? '))
    except Exception as e:
        return 'Amount must be a number.'
    state = input("What is the state? ")
    return tax_calc(amount, state)


if __name__ == '__main__':
    print(main())