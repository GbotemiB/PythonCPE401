import matplotlib.pyplot as plt


def division(input_a_param: str, input_b_param: str):
    input_a_param = binary_4bit_num(input_a_param)
    input_b_param = binary_4bit_num(input_b_param)
    a = [0] * 4
    b = [int(i) for i in input_b_param]
    q = [int(i) for i in input_a_param]
    dividend = [i for i in q]
    nB = [0] * 4

    print('Dividend ', q)
    print('Divisor ', b)
    # code of 2's complement of Divisor
    c = 1
    for i in range(3, -1, -1):
        nB[i], c = adds(xors(b[i], 1), 0, c)

    # main code start
    for cnt in range(4):
        # shift operation (left shift a, q)
        a, q = shifts(a, q)
        C = 0
        # subtraction operation (a=a-b) // beca
        for i in range(3, -1, -1):
            print(i)
            a[i], C = adds(a[i], nB[i], C)
        # check MSb of a
        if a[0] == 0:
            q[3] = 1  # set LSb of q
        else: #restore
            q[3] = 0  # set LSb of q
            c = 0
            # addition operation (a = a + b)
            for i in range(3, -1, -1):
                a[i], C = adds(a[i], b[i], C)
    # Result Display
    print('quotient: ', q)
    print('Remainder: ', a)

    # Plotting Result
    plt.subplot(2, 2, 1)
    plt.plot(dividend, 'y')
    plt.xlabel('Dividend')

    plt.subplot(2, 2, 2)
    plt.plot(b, 'b')
    plt.xlabel('Divisor')

    plt.subplot(2, 2, 3)
    plt.plot(q, 'r')
    plt.xlabel('quotient')

    plt.subplot(2, 2, 4)
    plt.plot(a, 'g')
    plt.xlabel('Remainder')

    # giving padding to subplots preventing the labels from being hidden
    plt.tight_layout()
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


def shifts(remainder, dividend):
    msb = dividend[0]
    for i in range(1, len(remainder)):
        temp = remainder[i]
        remainder[i - 1] = temp
    remainder[-1] = msb
    for i in range(1, len(dividend)):
        temp = dividend[i]
        dividend[i - 1] = temp
    dividend[-1] = 0
    return remainder, dividend


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
