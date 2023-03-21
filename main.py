def encode(num):
    list = str(num)
    encode_str = ''
    for i in list:
        new_list = int(i) + 3
        encode_str += str(new_list)
    return encode_str


if __name__ == "__main__":

    while True:
        print("Menu")
        print("-------------")
        print("1. Encode ")
        print("2. Decode ")
        print("3. Quit")

        option = int(input("Please enter an option:"))
        if option == 1:
            num = input("Please enter your password to encode:")
            encode(num)
            print("Your password has been encoded and stored!")
        # if option == 2:
        #     decode()
        #     print(f"The encoded password is {encode(num)}, and the original password is {num}.")
        if option == 3:
            break




