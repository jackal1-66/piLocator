#!/usr/bin/env python

## Old function to generate a file containing the digits of pi
## not used anymore, as well as its mandatory library mpmath
# from mpmath import mp
import os 

'''
def generate_pi(precision):
    mp.dps = int(precision)
    fname = "pi"+str(mp.dps)+".txt"
    if not os.path.exists(fname): 
        pi_str = str(mp.pi)   
        with open(fname, "w") as f:
            f.write(pi_str)
    return fname
'''

## Recursive read of files has been implemented to bypass GitHub limit
## of 100 MB per file size. This operation reduces marginally the performances
def load_pi(name, recursive = 1):
    if recursive > 1:
        string = ""
        for a in range(recursive):
            with open(name+str(a)+".txt", 'r') as f:
                string += f.read()
        return string          
    else:        
        with open(name, 'r') as f:
            return f.read()            

def easyPi(val, pi_str):
        #now check if number is contained in Pi
    try:
        index = pi_str.index(val)
        print("Found in pi with index: ", index)
    except ValueError:
        print("Not found in the first 1 billion and one digits of Pi.")

def main():
    number = input("Enter your number: ")
    pi_str = load_pi("piDigits/pi1e8_", 10)
    easyPi(number, pi_str)
    
if __name__ == "__main__":
    main()