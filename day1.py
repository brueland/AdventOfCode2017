'''
Wesley Brueland
4/11/18
Advent of Code 2017: Day 1
'''

def reverseCaptchaP1(input):
    StrInput = str(input)
    CaptchaSum = 0
    for index, val in enumerate(StrInput):
        if val == StrInput[index-1]:
            CaptchaSum += int(val)
    return CaptchaSum

def reverseCaptchaP2(input):
    StrInput = str(input)
    CaptchaSum = 0
    ModStr = len(StrInput)//2
    for index, val in enumerate(StrInput):
        if val == StrInput[index-ModStr]:
            CaptchaSum += int(val)
    return CaptchaSum


def captchaTest1():
    assert reverseCaptchaP1(1122) == 3
    assert reverseCaptchaP1(1111) == 4
    assert reverseCaptchaP1(1234) == 0
    assert reverseCaptchaP1(91212129) == 9

def captchaTest2():
    assert reverseCaptchaP2(1212) == 6
    assert reverseCaptchaP2(1221) == 0
    assert reverseCaptchaP2(123425) == 4
    assert reverseCaptchaP2(123123) == 12
    assert reverseCaptchaP2(12131415) == 4
    
captchaTest1()
captchaTest2()
