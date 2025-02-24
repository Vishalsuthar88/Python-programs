def printstr(str1):
    print(f"This is a str: {str}")
def addtwo(a,b):
    return a+b+10;
print(f"the value of __name__ is: {__name__}")
if __name__ == '__main__': # if this program is run then only __name__ value is main
    printstr("hello")
    result = addtwo(5,7)
    print(result)
