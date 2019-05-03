#!/usr/bin/env python
import argparse

def main():
    print("hello")

if __name__ == '__main__':
    # Demonstaration of potional argument.
    parser = argparse.ArgumentParser()
    parser.add_argument("Number1", help="First Number")
    parser.add_argument("Number2", help="Second Number")
    parser.add_argument("Operator", help="Operator",choices = ["+","-"])
    args = parser.parse_args()
    print(args.Number1)
    print(args.Number2)
    print(args.Operator)

    n1 = int(args.Number1)
    n2 = int(args.Number2)
    if args.Operator  == "+":
        print(n1+n2)
    elif args.Operator == "-":
        print(n1-n2)
    else:
        print('Bye')





''' call this program along with params and spaces between each param.
python posArgument.py 1 2 +
'''