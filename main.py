import sys

def logic(operation, int1, int2):
    operation = operation
    int1 = int1
    int2 = int2

    if operation == "m":
        answer = int1 * int2
        print "answer is %s" % answer

    elif operation == "a":
        answer = int1 + int2
        print "answer is %s" % answer

    elif operation == "d":
        answer = int1 / int2
        print "answer is %s" % answer

    elif operation == "s":
        answer = int1 - int2
        print "answer is %s" % answer

def user_input():
    operation = raw_input("operation (a)dd, (s)ubtract, (m)ultiply, (d)ivide: ")

    if operation != "a" or "s" or "m" or "d":
        print "invalid operation!"
        sys.exit()
    
    int1 = input("first integer: ")
    int2 = input("second integer: ")

    logic(operation, int1, int2)

user_input()
