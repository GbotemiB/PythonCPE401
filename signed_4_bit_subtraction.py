import subtractionFunction
import matplotlib.pyplot as plt
import numpy as np


def action():
    # filter input  to be binary and return flipped bit (LSB is in the front) so as to iterate from back
    first = input('input the first 4-bit number to subtract from  \n')
    second = input('input the second 4-bit number \n')
    [output, carry, sign] = subtractionFunction.subtraction(first, second)
    print("the subtraction of")
    print(f"   {first.zfill(4)}\n  -{second.zfill(4)}\n========\n  {sign}{output}")
    print("------------------")
    print(f"carry is {carry}")

    if sign == '-':
        sign = 1
    else:
        sign = 0
    label_bit = np.arange(4)[::-1]
    a = [int(i) for i in first][::-1]
    b = [int(i) for i in second][::-1]
    s = [sign] + [int(i) for i in output]
    s_label = ['sign'] + [str(i) for i in label_bit]
    fig, (in_a, in_b, output_c) = plt.subplots(1, 3)
    plot_a = in_a.bar(label_bit, a)
    in_a.set_xlabel('input a')
    plot_b =in_b.bar(label_bit, b)
    in_b.set_xlabel('subtracted input b')
    plot_c = output_c.bar(s_label, s)
    output_c.set_xlabel('output c')
    for bar in plot_b.patches:
        in_b.annotate(bar.get_height(),
                          (bar.get_x() + bar.get_width() / 2,
                           bar.get_height()), ha='center', va='center',
                          size=15, xytext=(0, 8),
                          textcoords='offset points')
    for bar in plot_a.patches:
        in_a.annotate(bar.get_height(),
                          (bar.get_x() + bar.get_width() / 2,
                           bar.get_height()), ha='center', va='center',
                          size=15, xytext=(0, 8),
                          textcoords='offset points')
    for bar in plot_c.patches:
        output_c.annotate(bar.get_height(),
                          (bar.get_x() + bar.get_width() / 2,
                           bar.get_height()), ha='center', va='center',
                          size=15, xytext=(0, 8),
                          textcoords='offset points')
    plt.show()


def start():
    try:
        action()
    except ValueError as err:
        print(f"{err} \n ====== ")
        start()


start()
