# These are comments made by Yaolu Shen.
def encode(num):
    list = str(num)
    encode_str = ''
    for i in list:
        new_list = int(i) + 3
        encode_str += str((new_list) % 10)
    return encode_str


def decoder(num):
    string2 = " "
    for i in range(len(num)):
        string2 += str((int(num[i]) - 3) % 10)
    return string2

if __name__ == "__main__":
    encoded_password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode ")
        print("2. Decode ")
        print("3. Quit")

        option = int(input("Please enter an option:"))
        if option == 1:
            num = input("Please enter your password to encode:")
            encoded_password = encode(num)
            print("Your password has been encoded and stored!")
        if option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.")
        if option == 3:
            break




