def move(n, a, b, c):
    step = (2 ** n) + 1
    for i in range (int(n/3+1)):

        if n % 2 == 0:
            if step > 0:
                print(a, " ---> ", b)   
                step = step - 1
                if step > 0:
                    print(a, " ---> ", c)
                    step = step - 1
                    if step > 0:
                        print(b, " ---> ", c)
                        step = step - 1
                    else:
                        return
                else:
                    return
            else:
                return
        elif n % 2 == 1:
            if step > 0:
                print(a, " ---> ", c)   
                step = step - 1
                if step > 0:
                    print(a, " ---> ", b)
                    step = step - 1
                    if step > 0:
                        print(b, " ---> ", c)
                        step = step - 1
                    else:
                        return
                else:
                    return
            else:
                return
        else:
            return


move(3, 'A', 'B', 'C')