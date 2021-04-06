import LogicalFunc


def subtraction(input_a_param: str, input_b_param: str):
    a = LogicalFunc.binary_4bit_num(input_a_param)
    b = LogicalFunc.binary_4bit_num(input_b_param)
    c = []
    carry: int = 1  # initialized as 1 so we would have the twos complement of b
    # we would change each bit of b to the ones complement
    for i in range(4):
        a_i = int(a[i])
        b_i = LogicalFunc.ones_complement_func(int(b[i]))
        # get sum of bit
        sum_i = LogicalFunc.sum_bits(a_i, b_i, carry)
        # get carry
        carry = LogicalFunc.get_carry(a_i, b_i, carry)
        # append bit sum to the output c array
        c.append(sum_i)
    sign = '+'
    if carry == 0:
        for i in range(4):
            c[i] = LogicalFunc.__generic_xor___(1, c[i])
        carry = 1
        for i in range(4):
            sum_new = LogicalFunc.sum_bits(c[i], 0, carry)
            # get carry
            carry = LogicalFunc.get_carry(c[i], 0, carry)
            c[i] = sum_new
        sign = '-'
    output = ''.join([str(c_i) for c_i in c][::-1])
    return [output, carry, sign]
