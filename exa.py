i = 2
while i < 10:
    j = 1
    while j < 10:
        print('{} * {} = {:2d}'.format(i, j, i * j), end=' ')
        j += 1
    print('\n')
    i += 1
    # while문을 사용한 구구단
