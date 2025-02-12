#f strings: string formating
name = "vishal"
numb = 58
msg = "This is %s and my roll no. is %s"%(name,numb)
print(msg)

#using .format
msg2 = "My name is {0} and roll no. is {1}"
result = msg2.format(name,numb)
print(result)

#using fstring : simplest
msg3 = f"Hello {name}, your roll no. is {numb}"
print(msg3)