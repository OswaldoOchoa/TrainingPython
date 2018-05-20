from itertools import groupby

def sum_consecutives(s):
    print(s)
    input([sum(group) for c, group in groupby(s)])
    input([group for c, group in groupby(s)])
    input([c for c, group in groupby(s)])
    input([max(group) for c, group in groupby(s)])
    input([min(group) for c, group in groupby(s)])
    s.insert(0,'$')
    counter=1
    iter0=1
    iter1=len(s)
    for n in range(len(s)):
        if s[iter1-iter0]==s[iter1-iter0-1]:
            counter+=1
            del s[iter1-iter0]
            iter1-=1
        elif s[iter1-iter0-1]!='$':
            s[iter1-iter0]*=counter
            iter0+=1
            counter=1
        else:
            s[iter1-iter0]*=counter
            del s[0]
            break
    return s
    
    
    #[sum(group) for c, group in groupby(s)]
    #[sum(g) for _, g in groupby(nums)]
    
sum_consecutives([1, 4, 4, 3, 4, 4, 0, 4, 3, 3, 1]) #,[1, 12, 0, 4, 6, 1]
sum_consecutives([1, 1, 7, 7, 3]) # [2, 14, 3]
#sum_consecutives([-5, -5, 7, 7, 12, 0]) #[-10, 14, 12, 0]
#sum_consecutives([3, 3, 3, 3, 1]),[12, 1]
#sum_consecutives([2, 2, -4, 4, 5, 5, 6, 6, 6, 6, 6, 1]),[4, -4, 4, 10, 30, 1]
#sum_consecutives([1, 1, 1, 1, 1, 3]),[5, 3]
#sum_consecutives([1, -1, -2, 2, 3, -3, 4, -4]),[1, -1, -2, 2, 3, -3, 4, -4]
#sum_consecutives([0, 1, 1, 2, 2]),[0, 2, 4]