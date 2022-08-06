def greet():
    print('hello')
greet()                           #hello



def greet(n):
    print('hello '+n)
greet('hi')                         #hello hi
greet('hey')                        #hello hey


def greet(n):
    print('hello '+n)
greet()                              #type error   greet() missing


def greet(n):
    print('age is '+str(n))
greet(25)                             #age is 25



def greet(*names):
    print('hey',names[0])
greet('python','function','set','tuple')              #hey python



def greet(*names):
    print('hello '+names[1])
greet('ashish','redddy','chey')                        #reddy



def details(n,a):
    print('Hey '+n+ '! Your age is '+str(a))
details('ashish', 24)                                      #Hey ashish! Your age is 24
details(n='hd',a=26)                                          #hey hd! your age is 26


def r(x,y):
    return print(x+y)
r(4,5)
print(r(5,6))                                                #9,11,none



a=[1,6,3,8,2]
a.sort()
print(a)                                                      #[1,2,3,6,8]
print(sorted([12,3,678,9]))                                   #3,9,12,678