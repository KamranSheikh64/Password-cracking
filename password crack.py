from brute import login



for i in range(999,10000):
    a = login(i)


    if a==True:
        print(f'your password is {i}')
        break
    else:
        print('check again')
