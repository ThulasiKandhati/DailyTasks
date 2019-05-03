#!/usr/bin/env python
import argparse

def main():
    print("hello")

if __name__ == '__main__':
    ''' Demonstaration of optional argument.
    Just include --before the argument to make it as a optional'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--Number1", help="First Number")
    parser.add_argument("--Number2", help="Second Number")
    parser.add_argument("--Operator", help="Operator",
                        choices = ["+","-"])
    args = parser.parse_args()
    print(args.Number1)
    print(args.Number2)
    print(args.Operator)
    if args.Number1 is None:
        n1 = 0
    else:
        n1 = int(args.Number1)
    if args.Number2 is None:
        n2 = 0
    else:
        n2 = int(args.Number2)
    if args.Operator  == "+":
        print(n1+n2)
    elif args.Operator == "-":
        print(n1-n2)
    else:
        print('Bye')



'''Should be called with along with argument name 
python optparse.py --Number1 10
python optparse.py --Number2 10
python optparse.py --Number1 10 --Number2 20 --Operator +

Adding choices in order to restrict user to choose aviliable options.Add choices argument.
Error Prompt : optparse.py: error: argument --Operator: invalid choice: '0' (choose from '+', '-')
'''

