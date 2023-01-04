def high():
    acu = 0
    val1 = input("Ingrese primer valor")
    val2 = input("Ingrese segundo valor")
    val3 = input("Ingrese tercer valor")
    val4 = input("Ingrese cuarto valor")
    val5 = input("Ingrese ultimo valor")
    arr = [int(val1), int(val2), int(val3), int(val4), int(val5)]
    while len(arr) != 2:
        for x in range(len(arr)):
            if arr[x] > arr[x+1]:
                arr.remove(arr[x+1])
            else:
                arr.remove(arr[x])
    print(arr)
    print(f"Los valores mas grandes son {arr[0]} y {arr[1]}")

high()