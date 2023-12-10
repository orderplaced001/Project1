while True:
    
    n = int(input('Input number (>1) >>> '))

    flag = n != 1
    d = 2
    while flag and d*d <= n:
        flag = n % d != 0
        d = d + 1

    print('Prime number: ', flag)





