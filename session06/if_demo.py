age = input('Please enter your age: ')

if int(age) >= 18:
    print('adult')
elif int(age) >= 6:
    print('teenager')
else:
    print('kid')
