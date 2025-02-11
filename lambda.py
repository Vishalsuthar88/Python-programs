#1
add = lambda x,y : x+y

print(add(5,4))
#2
def subtract(a,b):
    return a-b

print(subtract(9,1))
#3
def a_first(a):
    return a[1]
    
a = [[1,4],[6,2],[8,5]]
# a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)
