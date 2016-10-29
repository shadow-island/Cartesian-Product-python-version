# -*- coding: utf-8 -*-
'''
Created on 2016. 10. 9.

Input Format
https://www.hackerrank.com/challenges/maximize-it 
'''


#,,
input_lists = [[1,2],[3,4,5],[6,7]]
print('classic Method',input_lists) 

#pick_list
out_list = []

for layer in range(0,len(input_lists)):
        
    work_list = []
    if layer != 0:        
        import copy        
        work_list = copy.deepcopy(out_list)                                  
        out_list.clear()
    
    for x in input_lists[layer]:
        if layer == 0:
            out_list.append([x])
        else:                
            for pre_list in work_list:
                temp_list = copy.deepcopy(pre_list)
                #print('temp_list',temp_list)
                temp_list.append(x)                
                out_list.append(temp_list)         
                #print(out_list)
    #end of for

for i in range(0,len(out_list)):
    print(i+1,out_list[i])    
