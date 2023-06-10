from interface import CalculatorInterface

if __name__ == '__main__':
    print('----Welcome to your simple terminal calculator----')
    while True:
        input_1 = input('Enter the first number: ')
        input_2 = input('Enter the second number: ')
        action = input('Select the action and press enter -> Add (1), Subtract (2), Multiply (3), Divide (4):')
        result, errors = CalculatorInterface.perform(input_1=input_1, input_2=input_2, action=action)
        if errors:
            print(type(errors))
            print('Try again. Error encountered: ', errors)
        print('Result: ', result)

