def f(n):
    """
    f(0) = 0
    f(1) = 1
    f(2) = 1
    f(3) = 2
    f(4) = 3
    f(5) = 5
    f(n) = f(n-1) + f(n-2)
    """
    if n < 2:
        return n

    prev_number = 1
    current_number = 1
    # f(2)
    result = 1

    for idx in range(3, n+1):
        result = current_number + prev_number
        prev_number = current_number
        current_number = result

    return result

print("f(5)={}".format(f(5)))
print("f(10)={}".format(f(10)))
print("f(8181)={}".format(f(8181)))
