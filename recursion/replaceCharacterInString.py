# Here we will replace character on a given string with recursion

# Strings are immutable so there will be only one approach in this we will create new string

def replaceChar(s,x,y):
    l=len(s)
    if l==0:
        return s
    smallOutput=replaceChar(s[1:],x,y)
    if s[0]==x:
        return y+smallOutput
    else:
        return s[0]+smallOutput
    
s="abcdefabababa"
x="z"
y="#"
print(replaceChar(s,x,y))
