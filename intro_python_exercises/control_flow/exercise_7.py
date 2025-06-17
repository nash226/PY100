def integer_info(value):

    if value > 0 and value <= 50:
        print(f'{value} is between 0 and 50')
    elif value >= 51 and value <= 100:
        print(f'{value} is between 51 and 100')
    elif value > 100:
        print(f'{value} is greater than 100')
    else:
        print (f'{value} is less than 0')

integer_info(int(input('give me a numba: ')))
