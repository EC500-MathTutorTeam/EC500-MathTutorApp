import numpy as np
from TexttoWord import text2int
def get_number(word):   #Get numbers from the sentence
    word = text2int(word)
    temp_num = 0
    num_list = []
    flag = 0
    append_done = 1
    for i in word:
        if i.isdigit() == True:
            if flag == 0:
                temp_num = temp_num * 10 + int(i)
                append_done = 0
            else:
                temp_num = temp_num + int(i) / np.power(10, flag)
                flag += 1
                append_done = 0
        else:
            if i == '.':
                flag = 1
            elif append_done == 0:
                num_list.append(temp_num)
                flag = 0
                append_done = 1
                temp_num = 0
    if append_done == 0:
        num_list.append(temp_num)           
    return(num_list)

def sum_func(num_list:list):    #Simple addition
    sum_num = 0
    for i in num_list:
        sum_num += i
    return(sum_num)

def diff_func(num_list:list):   #Simple subtraction
    i = 1
    list_len = len(num_list)
    diff_num = num_list[0]
    while i < list_len:
        diff_num -= num_list[i]
        i += 1
    return(diff_num)

def product_func(num_list:list):    #Simple multiplying
    product_num = 1
    for i in num_list:
        product_num *= i
        i += 1
    return(product_num)

def quotient_func(num_list:list):   #Simple division
    i = 1
    list_len = len(num_list)
    quotient_num = num_list[0]
    while i < list_len:
        quotient_num /= num_list[i]
        i += 1
    return(quotient_num)

if __name__ == "__main__":
    word = 'add two to ten and multiply by ten'
    print(get_number(word))

