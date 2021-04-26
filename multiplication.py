import matplotlib.pyplot as plt


def multiplication(input_a_param: str, input_b_param: str):
    input_a_param = binary_4bit_num(input_a_param)
    input_b_param = binary_4bit_num(input_b_param)
    a = [0] * 8
    b = [0] * 8
    result = [0] * 8
    a[4:8] = [int(i) for i in input_a_param]
    copy_a = [i for i in a]
    b[4:8] = [int(i) for i in input_b_param]
    copy_b = [i for i in b]
    print('Multiplicand = ', a)
    print('\n')
    print('Multiplier = ', b)
    print('\n')
    print('*********************')

    if b[7] == 1:
        # print(f"{b[7]} the value of LSB b[0] , initializes the result as the value of A")  # debug
        result = [i for i in a]
    for i in range(6, 3, -1):  # 6 , 5 , 4
        if b[i] == 1:  # if the bit at that point is one shift and add
            # print(f"{b[i]} is the next the multiplier at position b[{7 - i}]")  # debug
            c = 0
            for j in range(7, -1, -1):  # this process is performing a = a + a .. ie a = 2a, shifting to the left by 1
                a[j], c = add_bit(a[j], a[j], c)
            # print(a, end=' a in this step after shifting\n')
            c = 0
            for j in range(7, -1, -1):
                result[j], c = add_bit(result[j], a[j], c)  # adding the shifted a to the result
        else:  # else just shift a
            c = 0
            for j in range(7, -1, -1):
                a[j], c = add_bit(a[j], a[j], c)
    print('\n')
    print('Multiplication result = ', result)
    print('\n')
    fig, (plot_a, plot_b, plot_result) = plt.subplots(3, 1)
    plot_a.plot(copy_a, 'g')
    plot_b.plot(copy_b, 'r')
    plot_result.plot(result)
    plot_result.set_xlabel('Result after multiplication')
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


def add_bit(a, b, c):
    res = xors(xors(a, b), c)
    car = ors(ands(a, b), ands(xors(a, b), c))
    return res, car


def binary_4bit_num(num: str):
    if len(num) > 4:
        raise ValueError('Input a four bit number')
    num = num.zfill(4)
    # return flipped binary (that is the LSB is in the front)
    return ''.join([__is_bit__(i) for i in num.strip()])


def __is_bit__(num: str):
    bit = int(num)
    if bit > 1:
        raise ValueError('input is not a binary input')
    else:
        return str(bit)
