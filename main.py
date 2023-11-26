# Decimal to binary converter

def main():
    decimal = 100
    dec_to_bin(decimal)

def dec_to_bin(dec_num):
    if not isinstance(dec_num,int) or dec_num < 0:
        print("Input must be integer and more than 0")
    elif dec_num == 0:
        print("0b0")
        return 0
    else:
        bin = ""
        while dec_num > 0:
            bin = str(dec_num % 2) + bin
            dec_num //= 2

        print("0b" + bin)
        return int(bin)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


