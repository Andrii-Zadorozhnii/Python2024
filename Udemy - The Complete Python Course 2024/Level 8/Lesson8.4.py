# n! -> 10 -> 10*9*8*....*1
# 1! -> 1
# 0! -> 1

def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = 5

print(factorial(x))

# f(5) -> 120
# -> n == 0? > NO
# else: 5 * f(4) => 5 * 24 = 120
# -> 4 == 0? > NO
# else: 4 * f(3) => 4 * 6 = 12
# -> 3 == 0? > NO
# else: 3 * f(2) => 3 * 2 = 6
# -> 2 == 0 > NO
# else: 2 * f(1) => 2 * 1 = 2
# -> 1 == 0 > NO
# else 1 * f(0) => 1 * 1 = 1
# -> 0 == = > YES, RETURN 1

