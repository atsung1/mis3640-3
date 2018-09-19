import math
def gcd(a,b):

    if a < b:
        r0 = b % a
        q0 = math.floor(b / a)
        if r0 == 0:
            return a
        else:
            gcd(a, r0)
    else:
        r0 = a % b
        q0 = math.floor(a / b)
        if r0 == 0:
            return b
        else:
            gcd(b, r0)

print(gcd(42, 36))
