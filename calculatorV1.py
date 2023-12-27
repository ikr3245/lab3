prodolzhit = 'yes'
while prodolzhit == 'yes':
    f_num = float(input("введите первое число "))
    oper = input("введите операцию ")
    sec_num = float(input("введите второе число "))
    if oper == '+':
        print(f_num + sec_num)
    elif oper == '-':
        print(f_num - sec_num)
    elif oper == '/':
        print(f_num / sec_num)
    elif oper == '*':
        print(f_num * sec_num)
    else:
        print("Error")
    prodolzhit = input("введите 'yes' чтоб продолжить, или что-то другое, что уйти ")
