def continue_test():
    while True:
        s=input('Enter something')
        if s =='quit':
            break
        if len(s)<3:
            print('to small')
            continue
        print('input kurang panjang')

        continue_test()
