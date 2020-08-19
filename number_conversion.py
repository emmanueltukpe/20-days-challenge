import random


def base():
    x = random.randint(2, 16)
    if x == 10:
        return base()
    else:
        return x


n = base()
print(n)


N = random.randint(1, 1000) #N is capitalized because I was following question protocol
print(N)


def convert_number_system():
    remainder_list = []
    sum_base_10 = N


    while sum_base_10 > 0:
        divided = sum_base_10 // n
        remainder_list.append(str(sum_base_10 % int(n)))
        sum_base_10 = divided

    return_number = ''
    
    if n >= 2:
        hex_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    for index, each in enumerate(remainder_list):
        for key, value in hex_dict.items():
            if each == str(key):
                remainder_list[index] = value
    else:
        for each in remainder_list[::-1]:
            return_number += each

        return (return_number)

base_converter = convert_number_system()
print (base_converter)



       
