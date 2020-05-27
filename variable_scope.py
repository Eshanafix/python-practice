#hello :)

#LEGB = Local, Enclosing, Global, Built-in order of checking

#local/global

x = 'global x'
z = 'global z'

def test():
    global z
    y = 'local y'
    x = 'local x'
    z = 'local z'
    global a
    a = 'global a'
    #print(y)
    print(x) # local
    

test()
#print(y) local so won't show
print(x) #global
print(z) # changed because global was called in the function
print(a)



#built-in
#key phrases used in pyhton liek print, min, max,type etc
#you can overide them by doing          def min():

#enclosing
#nested functions

def outer():
    b = 'outer b'
    d = 'outer d'
    def inner():
        nonlocal b
        #b = 'inner b'
        print(d)
        print(b)
    inner()
    print(b)

outer()