def h1(k, m=13, A=0.62):
    print(f'h1({k}) = └ 13 ({k} * 0.62 mod 1) ┘')
    temp = float()
    temp = k * A
    print(f'h1({k}) = └ 13 ({temp} mod 1) ┘')
    temp %= 1
    temp = round(temp, 3)
    print(f'h1({k}) = └ 13 ({temp}) ┘')
    temp *= m
    print(f'h1({k}) = └ {temp} ┘')
    temp = int(temp)
    print(f'h1({k}) = {temp} ')

def h2(k, m=11, A=0.62):
    print(f'h2({k}) = 1 + └ 11 ({k} * 0.62 mod 1) ┘')
    temp = float()
    temp = k * A
    print(f'h2({k}) = 1 + └ 11 ({temp} mod 1) ┘')
    temp %= 1
    temp = round(temp, 3)
    print(f'h2({k}) = 1 + └ 11 ({temp}) ┘')
    temp *= m
    print(f'h2({k}) = 1 + └ {temp} ┘')
    temp = int(temp)
    print(f'h2({k}) = 1 + {temp} ')
    temp = temp + 1
    print(f'h2({k}) = {temp} ')



K =[369, 119, 287, 712, 141, 503, 186, 295, 528, 625]

for k in K:
    print('On substituting the values: ')
    h1(k)
    
    print('\nCalculating h2')
    h2(k)

    print('\n\n')
