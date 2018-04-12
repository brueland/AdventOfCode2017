'''
Wesley Brueland
4/11/18
Advent of Code 2017: Day 1
'''

def reverse_captcha_p1(input):
    str_input = str(input)
    captcha_sum = 0
    for index, val in enumerate(str_input):
        if val == str_input[index-1]:
            captcha_sum += int(val)
    return captcha_sum

def reverse_captcha_p2(input):
    str_input = str(input)
    captcha_sum = 0
    mod_str = len(str_input)//2
    for index, val in enumerate(str_input):
        if val == str_input[index-mod_str]:
            captcha_sum += int(val)
    return captcha_sum


def captcha_test1():
    assert reverse_captcha_p1(1122) == 3
    assert reverse_captcha_p1(1111) == 4
    assert reverse_captcha_p1(1234) == 0
    assert reverse_captcha_p1(91212129) == 9

def captcha_test2():
    assert reverse_captcha_p2(1212) == 6
    assert reverse_captcha_p2(1221) == 0
    assert reverse_captcha_p2(123425) == 4
    assert reverse_captcha_p2(123123) == 12
    assert reverse_captcha_p2(12131415) == 4
    
captcha_test1()
captcha_test2()
