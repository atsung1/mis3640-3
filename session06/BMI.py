def findbmi():
    wt = input('Please enter your weight: ')
    ht = input('Please enter yor height: ')
    bmi = float(wt)/((float(ht)) ** 2)

    if bmi <= 18.5:
        print('Your BMI is ', bmi, 'and you are underweight.')
    elif bmi <= 24.9:
        print('Your BMI is ', bmi, 'and you are normal weight.')
    elif bmi <= 29.9:
        print('Your BMI is ', bmi, 'and you are overweight.')
    else:
        print('Your BMI is ', bmi, 'and you are obese.')

findbmi()