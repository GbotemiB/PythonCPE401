import matplotlib.pyplot as plt


def main():
    R = [0] * 8
    A = [0] * 8
    B = [0] * 8
    print('Enter First Number')
    for i in range(4, 8):  # you are only inputting the last four bit that is the lower nibble
        A[i] = int(input('Enter number'))
    print('Enter Second Number')
    for i in range(4, 8):
        B[i] = int(input('Enter number'))
    print('Multiplicand = ', A)
    print('\n')
    print('Multiplier = ', B)
    print('\n')
    print('*********************')
    plt.subplot(311)
    plt.plot(A, 'g')  # i don't think second parameter is needed .. you u
    plt.xlabel('Multiplicant')
    if B[7] == 1:
        print(f"{B[7]} the value of LSB b[0] , initializes the result as the value of A")  # debug
        R = [i for i in A]
    for i in range(6, 3, -1):  # 6 , 5 , 4
        if B[i] == 1:  # if the bit at that point is one shift and add
            print(f"{B[i]} is the next the multiplier at position b[{7 - i}]")  # debug
            c = 0
            for j in range(7, -1, -1):  # this process is performing a = a + a .. ie a = 2a, shifting to the left by 1
                A[j], c = adds(A[j], A[j], c)
            print(A, end=' A in this step after shifting\n')
            c = 0
            for j in range(7, -1, -1):
                R[j], c = adds(R[j], A[j], c)  # adding the shifted a to the result
        else:  # else just shift A
            c = 0
            for j in range(7, -1, -1):
                A[j], c = adds(A[j], A[j], c)
            print(R)
    print('\n')
    print('Multiplication result = ', R)
    print('\n')
    plt.subplot(3, 1, 2)
    plt.plot(B, 'r')
    plt.xlabel('Multiplier')
    plt.subplot(3, 1, 3)
    plt.plot(R)
    plt.xlabel('Result after multiplication')
    plt.show()


def ands(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


def xors(a, b):
    if a != b:
        return 1
    else:
        return 0


def ors(a, b):
    if a == 0 and b == 0:
        return 0
    else:
        return 1


def adds(a, b, c):
    res = xors(xors(a, b), c)
    car = ors(ands(a, b), ands(xors(a, b), c))
    return res, car


if __name__ == '__main__':
    main()
