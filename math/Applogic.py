from MathLogic import get_number, get_knowledge, sum_func, diff_func, product_func, quotient_func, random_test
from voicecontrol import get_voice
import time

def app_logic():
    print('Welcome to Math Tutor!')
    exit_signal = 0
    while exit_signal == 0:
        learn_signal = 0
        help_signal = 0
        add_signal = 0
        sub_signal = 0
        mul_signal = 0
        div_signal = 0
        print('What would you like to do ?')
        voice_input_0 = get_voice()
        if voice_input_0 == 'exit':
            exit_signal = 1
        elif voice_input_0 == 'I want to learn about math' or voice_input_0 == 'I want to learn about Mass' or voice_input_0 == 'I want to learn about the math' or voice_input_0 == 'I want to learn about the mass':
            while learn_signal == 0:
                print('What would you like to learn')
                voice_input_1 = get_voice()
                if voice_input_1 == 'addition':
                    print(get_knowledge('addition'))
                    time.sleep(5)
                    print('Do you want to test your addition skill')
                    voice_input_add = get_voice()
                    if voice_input_add == 'yes':
                        while add_signal == 0:
                            test, nums = random_test('addition')
                            print(test)
                            res_add = sum_func(nums)
                            voice_input_add_res = get_number(get_voice())
                            if not voice_input_add_res:
                                print('No input detected, the anwser should be:' + str(res_add) + ' Would you like to do more test?')
                                voice_input_add_test = get_voice()
                                if voice_input_add_test == 'no':
                                    add_signal = 1
                            elif voice_input_add_res[0] == res_add:
                                print('Correct! You are great at addition. Do you want to do more test?')
                                voice_input_add_test = get_voice()
                                if voice_input_add_test == 'no':
                                    add_signal = 1
                            elif voice_input_add_res[0] != res_add:
                                print('The anwser is not correct, the anwser should be:' + str(res_add) + ' Would you like to do more test?')
                                voice_input_add_test = get_voice()
                                if voice_input_add_test == 'no':
                                    add_signal = 1
                elif voice_input_1 == 'subtraction':
                    print(get_knowledge('subtraction'))
                    time.sleep(5)
                    print('Do you want to test your subtraction skill')
                    voice_input_sub = get_voice()
                    if voice_input_sub == 'yes':
                        while sub_signal == 0:
                            test, nums = random_test('subtraction')
                            print(test)
                            res_sub = diff_func(nums)
                            voice_input_sub_res = get_number(get_voice())
                            if not voice_input_sub_res:
                                print('No input detected, the anwser should be:' + str(res_sub) + ' Would you like to do more test?')
                                voice_input_sub_test = get_voice()
                                if voice_input_sub_test == 'no':
                                    sub_signal = 1
                            elif voice_input_sub_res[0] == res_sub:
                                print('Correct! You are great at subition. Do you want to do more test?')
                                voice_input_sub_test = get_voice()
                                if voice_input_sub_test == 'no':
                                    sub_signal = 1
                            elif voice_input_sub_res[0] != res_sub:
                                print('The anwser is not correct, the anwser should be:' + str(res_sub) + ' Would you like to do more test?')
                                voice_input_sub_test = get_voice()
                                if voice_input_sub_test == 'no':
                                    sub_signal = 1
                elif voice_input_1 == 'multiplication':
                    print(get_knowledge('multiplication'))
                    time.sleep(5)
                    print('Do you want to test your multiplication skill')
                    voice_input_mul = get_voice()
                    if voice_input_mul == 'yes':
                        while mul_signal == 0:
                            test, nums = random_test('multiplication')
                            print(test)
                            res_mul = product_func(nums)
                            voice_input_mul_res = get_number(get_voice())
                            if not voice_input_mul_res:
                                print('No input detected, the anwser should be:' + str(res_mul) + ' Would you like to do more test?')
                                voice_input_mul_test = get_voice()
                                if voice_input_mul_test == 'no':
                                    mul_signal = 1
                            elif voice_input_mul_res[0] == res_mul:
                                print('Correct! You are great at mulition. Do you want to do more test?')
                                voice_input_mul_test = get_voice()
                                if voice_input_mul_test == 'no':
                                    mul_signal = 1
                            elif voice_input_mul_res[0] != res_mul:
                                print('The anwser is not correct, the anwser should be:' + str(res_mul) + ' Would you like to do more test?')
                                voice_input_mul_test = get_voice()
                                if voice_input_mul_test == 'no':
                                    mul_signal = 1
                elif voice_input_1 == 'division':
                    print(get_knowledge('division'))
                    time.sleep(5)
                    print('Do you want to test your division skill')
                    voice_input_div = get_voice()
                    if voice_input_div == 'yes':
                        while div_signal == 0:
                            test, nums = random_test('division')
                            print(test)
                            res_div = quotient_func(nums)
                            voice_input_div_res = get_number(get_voice())
                            if not voice_input_div_res:
                                print('No input detected, the anwser should be:' + str(res_div) + ' Would you like to do more test?')
                                voice_input_div_test = get_voice()
                                if voice_input_div_test == 'no':
                                    div_signal = 1
                            elif voice_input_div_res[0] == res_div:
                                print('Correct! You are great at divition. Do you want to do more test?')
                                voice_input_div_test = get_voice()
                                if voice_input_div_test == 'no':
                                    div_signal = 1
                            elif voice_input_div_res[0] != res_div:
                                print('The anwser is not correct, the anwser should be:' + str(res_div) + ' Would you like to do more test?')
                                voice_input_div_test = get_voice()
                                if voice_input_div_test == 'no':
                                    div_signal = 1
                elif voice_input_1 == 'exit math learning':
                    learn_signal = 1
                elif voice_input_1 == 'exit':
                    learn_signal = 1
                    exit_signal = 1
                else:
                    print('Could not recognize your command, please try again')
        elif voice_input_0 == 'help me with math problems':
            while help_signal == 0:
                print('What kind of math problems?')
                voice_input_help = get_voice()
                if voice_input_help == 'addition':
                    print('Please provide the numbers')
                    voice_input_add_numbers = get_voice()
                    add_numbers = get_number(voice_input_add_numbers)
                    res_help_add = sum_func(add_numbers)
                    print('The anwser is '+ str(res_help_add))
                elif voice_input_help == 'multiplication':
                    print('Please provide the numbers')
                    voice_input_mul_numbers = get_voice()
                    mul_numbers = get_number(voice_input_mul_numbers)
                    res_help_mul = product_func(mul_numbers)
                    print('The anwser is '+ str(res_help_mul))
                elif voice_input_help == 'subtraction':
                    print('Please provide the numbers')
                    voice_input_sub_numbers = get_voice()
                    sub_numbers = get_number(voice_input_sub_numbers)
                    res_help_sub = diff_func(sub_numbers)
                    print('The anwser is '+ str(res_help_sub))
                elif voice_input_help == 'division':
                    print('Please provide the numbers')
                    voice_input_div_numbers = get_voice()
                    div_numbers = get_number(voice_input_div_numbers)
                    res_help_div = quotient_func(div_numbers)
                    print('The anwser is '+ str(res_help_div))
                elif voice_input_help == 'exit':
                    help_signal = 1
                print('Still need help with math problems?')
                voice_input_math_help = get_voice()
                if voice_input_math_help == 'no':
                    help_signal = 1
            
    print('Thanks for using Math Tutor, see you next time')

if __name__ == "__main__":
    app_logic()