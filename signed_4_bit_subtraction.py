import LogicalFunc
import subtractionFunction


def action():
    # filter input  to be binary and return flipped bit (LSB is in the front) so as to iterate from back
    first = input('input the first 4-bit number to subtract from  \n')
    second = input('input the second 4-bit number \n')
    [output, carry, sign] = subtractionFunction.subtraction(first, second)
    print("the subtraction of")
    print(f"   {first.zfill(4)}\n  -{second.zfill(4)}\n========\n  {sign}{output}")
    print("------------------")
    print(f"carry is {carry}")


def start():
    try:
        action()
    except ValueError as err:
        print(f"{err} \n ====== ")
        start()


start()
