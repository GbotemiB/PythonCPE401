# Function get 4bit binary num of an input
import operator


def binary_4bit_num(num: str):
    if len(num) > 4:
        raise ValueError('Input a four bit number')
    num = num.zfill(4)
    # return flipped binary (that is the LSB is in the front)
    return ''.join([__is_bit__(i) for i in num.strip()][::-1])


def __is_bit__(num: str):
    bit = int(num)
    if bit > 1:
        raise ValueError('input is not a binary input')
    else:
        return str(bit)


def get_carry(a_bit: int, b_bit: int, carry_old: int):
    # carry is equal to or(and(a[i],b[i]),and(xor(a[i],b[i]),carry_old))
    carry_new: int = operator.or_((a_bit and b_bit), (operator.xor(a_bit, b_bit) and carry_old))
    return carry_new


def sum_bits(a_bit: int, b_bit: int, carry_bit: int):
    # sum is equal to xor(xor(a[i],b[i]),carry)
    sum_bit: int = operator.xor(operator.xor(a_bit, b_bit), carry_bit)
    return sum_bit
