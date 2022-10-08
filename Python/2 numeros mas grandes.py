def solution():
    a = 2
    b = 3
    c = 2
    d = 1
    e = 6
    f = 2
    inputArray = [a, b, c, d, e, f]
    maximo = max(inputArray)
    inputArray.remove(maximo)
    max2 = max(inputArray)
    print(max2 * maximo)


solution()
