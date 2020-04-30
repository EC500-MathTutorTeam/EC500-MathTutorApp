import numpy as np
from TexttoWord import text2int
import json
import random

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

def get_knowledge(cat):            #Return math knowledge
    f = open('MathKnowledge.json')
    data = json.load(f)
    return data[cat]

def random_test(cat):              #Test users math skills
    if cat == 'addition':
        paras = random.randrange(2,4,1)
        nums = []
        i = 0
        test = 'what is the sum of '
        while i < paras:
            nums.append(random.randrange(0,100,1))
            i += 1
        ii = 0
        while ii < paras - 1:
            test = test + str(nums[ii]) + ' '
            ii += 1
        test = test + 'and ' + str(nums[paras - 1])
        return test, nums
    else:
        if cat == 'subtraction':
            paras = 2
            nums = []
            nums.append(random.randrange(50,100,1))
            nums.append(random.randrange(1,49,1))
            test = 'what is the differen between ' + str(nums[0]) + ' and ' + str(nums[1])
            return test, nums
        elif cat == 'multiplication':
            paras = 2
            nums = []
            nums.append(random.randrange(1,10,1))
            nums.append(random.randrange(2,10,1))
            test = 'what is the product of ' + str(nums[0]) + ' and ' + str(nums[1])
            return test, nums
        else:
            paras = 2
            nums = []
            nums.append(random.randrange(2,20,2))
            nums.append(random.randrange(2,10,2))
            test = 'what is the quotient of ' + str(nums[0]) + ' and ' + str(nums[1])
            return test, nums
if __name__ == "__main__":          #Testing functionalities
    word = "the product of one hundred and nineteen"
    print(get_number(word))
    print(get_knowledge('addition'))
    print(random_test('addition'))

