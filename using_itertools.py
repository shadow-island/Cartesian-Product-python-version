# -*- coding: utf-8 -*-

#-debug-------------------------------------
is_simulation_mode = False
is_simulation_mode = True
#---------------------------------------
# based on 
# https://www.hackerrank.com/challenges/maximize-it
 
input_data_text = \
'''
3
2 5 4
3 7 8 9 
5 5 7 8 9 10 
'''


def p(obj, *therest):
    if is_simulation_mode:
        print('Debug:',obj, *therest)
    return

import collections 
input_q = collections.deque()
input_data = input_data_text.split('\n')
for i in input_data:
    if i == '':
        input_data.remove(i)
for i in input_data:    
    input_q.appendleft(i) 
# 
def input_from_both():  
    if is_simulation_mode:
        return input_q.pop()        
    else:       
        return input()

#- util -------------------------------
# number casting
def int_cast(p_list):
    for i in range(len(p_list)):
        p_list[i] = int(p_list[i]) 
    return p_list    
#- main -------------------------------
p('Start!!')

k_lists = []
for _ in range(int(input_from_both())):
    k_lists.append(int_cast(input_from_both().split()))
    
summ = 0
import itertools
for x in itertools.product(*k_lists):
    print(x,sum(x))
    summ = max(summ, sum(x))
p('End!!')
