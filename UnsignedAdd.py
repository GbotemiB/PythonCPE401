import LogicalFunc

try:

    # filter input  to be binary and return flipped bit (LSB is in the front) so as to iterate from back
    first = input('input the first 4-bit number \n')
    a = LogicalFunc.binary_4bit_num(first)
    second = input('input the second 4-bit number \n')
    b = LogicalFunc.binary_4bit_num(second)

    c = []
    carry: int = 0
    for i in range(4):
        a_i = int(a[i])
        b_i = int(b[i])
        # get sum of bit
        sum_i = LogicalFunc.sum_bits(a_i, b_i, carry)
        # get carry
        carry = LogicalFunc.get_carry(a_i, b_i, carry)
        # append bit sum to the output c array
        c.append(sum_i)

    output = ''.join([str(c_i) for c_i in c][::-1])
    print("the sum of")
    print(f"   {first.zfill(4)}\n  +{second.zfill(4)}\n========\n {carry} {output}")
    print("------------------")
    print(f"carry is {carry}")

except ValueError as err:
    print(err)
