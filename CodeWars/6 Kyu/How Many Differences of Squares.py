import math

def count_squareable(n):
    output = n-1-len(range(2,n,4)) if (n-2)%4==0 else n-len(range(2,n,4))
    print(output)
         
         
         
count_squareable(4) #3
count_squareable(5) #4
count_squareable(40) #30
count_squareable(20) #15
count_squareable(10) #7
count_squareable(50) #37
count_squareable(500) #375
count_squareable(537) #403
count_squareable(6427) #4820
count_squareable(45000) #33750