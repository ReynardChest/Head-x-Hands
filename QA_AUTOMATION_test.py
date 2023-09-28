import random as rnd
   
def sort_array_by_parity(array, array_num):
    sorted_array = array
        
    if array_num%2 == 0:
        sorted_array.sort(reverse = True)       
    elif array_num%2 != 0:
        sorted_array.sort(reverse = False)
        
    return sorted_array
        
def form_array(array_length):
    min_val = -10000
    max_val = 10000
    formed_array =  [rnd.randint(min_val, max_val) for _ in range(array_length)]
        
    return formed_array
    
def form_massive(num_of_iter):
    unused_len =list(range(0, num_of_iter*10))
    used_len = rnd.sample(unused_len, num_of_iter)
    formed_massive = []
    array_num = 0
        
    for i in used_len:            
        cur_array = form_array(i)
        sort_array_by_parity(cur_array,array_num)
        array_num += 1
        formed_massive.append(cur_array)
        
    return formed_massive
