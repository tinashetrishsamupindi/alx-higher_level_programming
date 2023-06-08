#!/usr/bin/python3 
 if __name__ == "__main__": 
     from calculator_1 import sub, add, div, mul 
     import sys 
     c = len(sys.argv) - 1 
     if c != 3: 
         print("Usage: ./100-my_calculator.py <a> <operator> <b>") 
         sys.exit(1) 
     a = int(sys.argv[1]) 
     b = int(sys.argv[3]) 
     ops = "+-*/" 
     if sys.argv[2] not in ops: 
         print("Unknown operator. Available operators: +, -, * and /") 
         sys.exit(1) 
     if sys.argv[2] == "+": 
         print("{} + {} = {}".format(a, b, add(a, b))) 
     if sys.argv[2] == "-": 
         print("{} - {} = {}".format(a, b, sub(a, b))) 
     if sys.argv[2] == "*": 
         print("{} * {} = {}".format(a, b, mul(a, b))) 
     if sys.argv[2] == "/": 
         print("{} / {} = {}".format(a, b, div(a, b)))
