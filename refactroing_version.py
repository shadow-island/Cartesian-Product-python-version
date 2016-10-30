# -*- coding: utf-8 -*-
'''
Created on 2016. 10. 9~

Input Format
https://www.hackerrank.com/challenges/maximize-it 
'''
# after making the first final code, I've found similar pseudo code 
# so, I am refactroing more

#
input_lists = [[1,2],[3,4,5],[6,7]]
print('classic Method',input_lists) 

out_lists = []

# Create the initial result filled with the first set of numbers
for x in input_lists[0]:
    out_lists.append([x])

# Iterate over the following sets to permutate over
for layer in range(1,len(input_lists)):        
    work_lists = []
    import copy
    for x in input_lists[layer]:             
        for old_list in out_lists:            
            new_list = copy.deepcopy(old_list)
            new_list.append(x)                
            work_lists.append(new_list)  
    out_lists = copy.deepcopy(work_lists)
    #end of for

for i in range(0,len(out_lists)):
    print(i+1,out_lists[i])    
