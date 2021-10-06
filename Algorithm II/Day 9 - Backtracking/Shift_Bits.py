n = int(input("Enter n: "))
for i in range(2**n, 2**(n + 1)):
    # generate bitmask, from 0..00 to 1..11
    print(i, bin(i))
    bitmask = bin(i)[3:]
    print(bitmask)