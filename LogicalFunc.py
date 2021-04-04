# Function get 4bit binary num of an input

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
    carry_new: int = __generic_or__((__generic_and__(a_bit, b_bit)),
                                    __generic_and__(__generic_xor___(a_bit, b_bit), carry_old))
    return carry_new


def sum_bits(a_bit: int, b_bit: int, carry_bit: int):
    # sum is equal to xor(xor(a[i],b[i]),carry)
    sum_bit: int = __generic_xor___(__generic_xor___(a_bit, b_bit), carry_bit)
    return sum_bit


# a function that return  OR for two bits
def __generic_or__(a_bit: int, b_bit: int):
    if (a_bit == 0) and (b_bit == 0):
        return 0
    else:
        return 1


# a function that return exclusive OR for two bits
def __generic_xor___(a_bit: int, b_bit: int):
    if a_bit != b_bit:
        return 1
    else:
        return 0


# a function that return AND for two bits
def __generic_and__(a_bit: int, b_bit: int):
    if (a_bit == 1) and (b_bit == 1):
        return 1
    else:
        return 0


def ones_complement(bit: int):
    return __generic_xor___(1, bit)


def decimal_to_binary(n):
    if int(n) < 2**4:
        return "{0:b}".format(int(n)).zfill(4)
    raise ValueError('larger than four bit')

