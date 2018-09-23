# result = 0

# for i in range(1, 1001):
#     if i % 2 == 1:

#         print('current number to be added:', i)
#         result = result + i
#         print('the after-result: ', result)
#     else:
#         result = result

# print('the final result: ', result)
    
# result = 1

# for i in range(1, 11):
#     result = result * i

# print('factorial is', result)

# import time

# def countdown(n):
#     while n > 0:
#         print(n)
#         time.sleep(1)
#         n = n - 1
#     print('Blastoff!')

# countdown(5)


while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print("Done!")