
#? immutable 
# str 
# int
# float
# bool
# bytes
# tuple

#? mutable
#! list 
x = [i for i in range(10) if i % 2 == 0]
print(x)

#!set is a collection which is unordered, unchangeable, and unindexed. No duplicate members
myset = {"apple", "apple", "banana", "cherry"}
print(myset)
# dict


#? *args - accepts any numbers of arguments and store them as a tuple
def complicated_function(x, y, *args):
    print(x, y , args)
    pass
# complicated_function(1, 2, 3, 4 ,5)

#? **kwargs
def some_function(*args, **kwargs):
    print(args, kwargs)
    pass
# some_function(5,6, x=1, s='hello', b=True)

#? * asterisk
def asterisk_function(a,b, c = True, d = False):
    print(a, b , c, d)
    pass
#the "*" helps identify the 1 and 2 as two elements
# the seond "**" indicates the value of the dictionary, "*" indicates the key of the dictionary 
asterisk_function(*[1,2], **{"c": "hello", "d": "cool"})
    
