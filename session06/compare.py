def check(a,b):

    if isinstance(a, str) or isinstance(b, str):
        print('String involved')
    elif a > b:
        print('bigger')
    elif a < b:
        print('smaller')
    else:
        print('equal')

check(1,3)
check(3,1)
check(1,1)
check('iii',1)