for i in range(0, 13, 3):
    if len(str(i)) == 1:
        print('0{}'.format(i))
    else:
        print(i)