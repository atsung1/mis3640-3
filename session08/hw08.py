# Excercise 3
# m = input("What is title you want to capitalize?")
# print(m.title())

# m = float(input('How much does it cost? '))
# print('It costs $'+'{:,}'.format(m)+'.')

# 'test'.find('st')


#Exercise 4-1
# def price(a):
#     p = 0
#     for i in a:
#         if ord(i)-96 > 0:
#             p = (ord(i)-96) + p
#     print(a + ' '+ '$' + str(p))


# price('bananas')
# price('rice')
# price('paprika')
# price('potato chips')
# print('total '+'$301')


#Excercise 4-2
# def price(a):
#     p = 0
#     for i in a:
#         if ord(i)-96 > 0:
#             p = (ord(i)-96) + p
#     print('{:<15} {:<2} {:<3}'.format(a, ' $', str(p)))


# price('bananas')
# price('rice')
# price('paprika')
# price('potato chips')
# print('{:<15} {:<2} {:<3}'.format('total', ' $', '301'))


#Excersice 4-3
def price(a):
    p = 0
    for i in a:
        if ord(i)-96 > 0:
            p = (ord(i)-96) + p
    if len(a) < 8:
        print('{:<10} {:<2} {:<3}'.format(a, ' $', str(p)))
    else:
        print('{:<15} {:<2} {:<3}'.format(a, ' $', str(p)))


price('bananas')
price('rice')
price('paprika')
print('{:<10} {:<2} {:<3}'.format('total', ' $', '159'))
