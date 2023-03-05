while True:
    n = int(input('Enter a value: '))

    print('Number\tSquare\tCube')

    for i in range(1, n+1):
        square = i ** 2
        cube = i ** 3
        print(f'{i}\t{square}\t{cube}')

    choice = input('Do you want to continue? (y/n): ')
    if choice.lower() == 'n':
        break