def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    mid = int(len(my_list)/2)
    higher = len(my_list) - 1
    lower = 0

    while (higher - lower > 1):
        if x < my_list[mid]:
            higher = mid
            mid = int((higher + lower)/2)
        elif x > my_list[mid]:
            lower = mid
            mid = int((lower + higher)/2)
        else:
            return mid

    if my_list[lower] == x:
        return lower
    elif my_list[higher] == x:
        return higher

test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()
print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None