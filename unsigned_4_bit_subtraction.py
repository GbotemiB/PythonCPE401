import subtractionFunction
import matplotlib.pyplot as plt
import numpy as np


def action():
    # filter input  to be binary and return flipped bit (LSB is in the front) so as to iterate from back
    input_a = input('input the first 4-bit number to subtract from  \n')
    input_b = input('input the second 4-bit number \n')
    [output, carry, sign] = subtractionFunction.subtraction(input_a, input_b)
    print("the subtraction of")
    print(f"   {input_a.zfill(4)}\n  -{input_b.zfill(4)}\n========\n  {sign}{output}")
    print("------------------")
    print(f"carry is {carry}")

    if sign == '-':
        sign = 1
    else:
        sign = 0
    label_bit = np.arange(4)[::-1]
    a = [int(i) for i in input_a][::-1]
    b = [int(i) for i in input_b][::-1]
    s = [sign] + [int(i) for i in output]
    s_label = ['sign'] + [str(i) for i in label_bit]
    fig, (in_a, in_b, output_c) = plt.subplots(1, 3)
    in_a.bar([str(i) for i in label_bit], a)
    in_a.set_xlabel('input a')
    in_b.bar([str(i) for i in label_bit], b)
    in_b.set_xlabel('subtracted input b')
    output_c.bar(s_label, s)
    output_c.set_xlabel('output c')
    plt.show()


def start():
    try:
        action()
    except ValueError as err:
        print(f"{err} \n ====== ")
        start()


start()
