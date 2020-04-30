from MathLogic import get_number, get_knowledge, sum_func, diff_func, product_func, quotient_func, random_test
from voicecontrol import get_voice
import time

def app_logic():
    print('Welcome to Math Tutor!')
    exit_signal = 0
    learn_signal = 0
    help_signal = 0
    add_signal = 0
    sub_signal = 0
    mul_signal = 0
    div_signal = 0
    while exit_signal == 0:
        print('What would you like to do ?')
        voice_input_0 = get_voice()
        if voice_input_0 == 'exit':
            exit_signal = 1
        elif voice_input_0 == 'I want to learn about math':
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
                            if voice_input_add_res[0] == res_add:
                                print('Correct! You are great at addition. Do you want to do more test?')
                                voice_input_add_test = get_voice()
                                if voice_input_add_test == 'no':
                                    add_signal = 1
                            elif voice_input_add_res != res_add:
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
                            if voice_input_sub_res[0] == res_sub:
                                print('Correct! You are great at subtraction. Do you want to do more test?')
                                voice_input_sub_test = get_voice()
                                if voice_input_sub_test == 'no':
                                    sub_signal = 1
                            elif voice_input_sub_res != res_sub:
                                print('The anwser is not correct, the anwser should be:' + str(res_sub) + 'Would you like to do more test?')
                                voice_input_sub_test = get_voice()
                                if voice_input_sub_test == 'no':
                                    sub_signal = 1
                elif voice_input_1 == 'multiplication':
                    print(get_knowledge('multiplication'))
                    time.sleep(5) #copy
                    print('Do you want to test your multiplication skill')
                    voice_input_mul = get_voice()
                    if voice_input_mul == 'yes':
                        while mul_signal == 0:
                            test, nums = random_test('multiplication')
                            print(test)
                            res_mul = product_func(nums)
                            voice_input_mul_res = get_number(get_voice())
                            if voice_input_mul_res[0] == res_mul:
                                print('Correct! You are great at multiplication. Do you want to do more test?')
                                voice_input_mul_test = get_voice()
                                if voice_input_mul_test == 'no':
                                    mul_signal = 1
                            elif voice_input_mul_res != res_mul:
                                print('The anwser is not correct, the anwser should be:' + str(res_mul) + 'Would you like to do more test?')
                                voice_input_mul_test = get_voice()
                                if voice_input_mul_test == 'no':
                                    mul_signal = 1
                elif voice_input_1 == 'division':
                    print(get_knowledge('division'))
                    time.sleep(5) #copy
                    print('Do you want to test your division skill')
                    voice_input_div = get_voice()
                    if voice_input_div == 'yes':
                        while div_signal == 0:
                            test, nums = random_test('division')
                            print(test)
                            res_div = sum_func(nums)
                            voice_input_div_res = get_number(get_voice())
                            if voice_input_div_res[0] == res_div:
                                print('Correct! You are great at division. Do you want to do more test?')
                                voice_input_div_test = get_voice()
                                if voice_input_div_test == 'no':
                                    div_signal = 1
                            elif voice_input_div_res != res_div:
                                print('The anwser is not correct, the anwser should be:' + str(res_div) + 'Would you like to do more test?')
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
    print('Thanks for using Math Tutor, see you next time')

if __name__ == "__main__":
    app_logic()