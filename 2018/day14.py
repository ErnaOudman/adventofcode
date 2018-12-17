# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

start =  '37'
recipes = '030121'

def get_next(r_list, recipes, l1,l2):
    # while list(recipes) != r_list[-7:]:
    while len(r_list) <= int(recipes)+10:
        newval = str(int(r_list[l1]) + int(r_list[l2]))
        r_list += list(newval)
        l1 = (int(r_list[l1])+l1+1) % len(r_list)
        l2 = (int(r_list[l2])+l2+1) % len(r_list)
        
    else:
        return ''.join(r_list[int(recipes):int(recipes)+10])
        #return r_list
#    


#
def get_index(r_list, recipes, l1,l2):
    # while list(recipes) != r_list[-7:]:
    while r_list[-len(recipes):] != list(recipes):
        newval = str(int(r_list[l1]) + int(r_list[l2]))
        r_list += list(newval)
        l1 = (int(r_list[l1])+l1+1) % len(r_list)
        l2 = (int(r_list[l2])+l2+1) % len(r_list)
        
    else:
        return ''.join(r_list).index(recipes)
#
#    
b = get_index(list(start), recipes,0,1)
print(b)