from division import division


def start():
    input_a = input('input the first number \n')
    input_b = input('input the second number \n')
    division(input_a, input_b)


def main():
    try:
        start()
    except ValueError as err:
        print(f"{err} \n ====== ")
        main()


if __name__ == '__main__':
    main()
