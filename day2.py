'''
Wesley Brueland
4/11/18
Advent of Code 2017: Day 2
'''
import pandas as pd

def check_sum_p1(input_path):
    input_df = pd.read_csv(input_path,
                           sep = ' |\t',
                           header=None,
                           engine='python')
    return sum(input_df.max(axis=1)-input_df.min(axis=1))

def check_sum_p2(input_path):
    input_df = pd.read_csv(input_path,
                           sep = ' |\t',
                           header=None,
                           engine='python')
    check_sum = 0
    for row in input_df.T:
        bool_list = [(i%input_df.iloc[row]==0) for i in input_df.iloc[row]]
        bool_index = [index for index, i in enumerate(bool_list) if sum(i)==2 ][0]
        mod_index = input_df.iloc[row][bool_list[bool_index]==True].values
        check_sum += max(mod_index)/min(mod_index)
    return check_sum

def test_check_sum_p1():
    assert check_sum_p1('day2_inputs_p1.txt') == 18

def test_check_sum_p2():
    assert check_sum_p2('day2_inputs_p2.txt') == 9

test_check_sum_p1()
test_check_sum_p2()


