'''Collatz Conjecture - Start with a number n > 1. 
Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 
'''
from matplotlib.pyplot import flag


step = 0
def mainfunc():
    
    n = int(input("Enter desired number\n"))   #Enter number to collatz conjecture...
   # while(n != 1):
    result = collatz_conj(n)
    print(F"REQUIRED STEPS TO REACH 1 FROM NUMBER {n} ARE: {result}")

def collatz_conj(n):                        # Algorithm Implementation
    global step
    bool1 = True
    while bool1 == True:
        if(n==1):
            print("Task Completed")         # if n has value 1 then exit
            #step += 1
            bool1 = False
        else:
            if(n%2 == 0):
                n = n/2
                step += 1
            else:
                n = (n*3)+1
                step += 1
    return step
        
            
mainfunc()
            
            
            