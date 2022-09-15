while True:
    print ('Введите первое число: ')
    x = float(input())
    print ('Введите знак операции: ')
    s = input()
    print ('Введите второе число: ')
    y = float(input())
    if s in ('+', '-', '*', '/'):
        if s == '+':
            print ('Ответ:',x+y)
        elif s == '-':
            print ('Ответ:',x-y)
        elif s == '*':
            print ('Ответ:',x*y)
        elif s == '/':
            if y != 0:
                print ('Ответ:',x/y)
            else:
                print("Ошибка! На 0 делить нельзя")
    else:
        print("Неверный знак операции!")