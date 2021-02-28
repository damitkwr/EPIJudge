from test_framework import generic_test
import functools

def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def count_no_of_steps(stairs_left, max_steps=maximum_step):
        if stairs_left <= 1:
            return 1

        return sum(count_no_of_steps(stairs_left-step) for step in range(1, min(max_steps, stairs_left)+1))
        
    
    temp = 0
    res = [1] 
    n = top
    m = maximum_step  
    for i in range(1, n + 1):
        s = i - m - 1
        e = i - 1
        if (s >= 0):
            temp -= res[s] 
        temp += res[e] 
        res.append(temp) 
         
    return res[n] 
    # stepsTable = [0] * top+1
    # for i in range(1, maximum_step+1):


    # def count_steps_table_way(stairs_left, max_steps=maximum_step):
        

    return count_no_of_steps(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
