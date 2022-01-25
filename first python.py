############################variables
x=34
y=3265.255
z='xyz'
print(type(x))
print(type(y))
print(type(z))
                  
a = [1,2,3,4]
print(a,type(a))
b=(1,2,3,4)       #tuple, its values are unchangeable 
print(b,type(b))
a[3]=5           #changing the value in list
print(a)

(A,B,C) = 10,20,30  #many variables with values
print(A, B, C)

                    #file pointers need to learn

(a1,a2)=12.2, 2.3
print('not int ',a1/a2)
print('int ',a1//a2)   #this returns the integer result

String = "Waliul Hasan"
lenth = len(String)
print(lenth)

print(String[0])   #0 index value
print(String[0:6]) #0 to 6 index value
print(String[0:])  #0 to last positioon
print(String[7:])  #7 to last position

################################################ Number

g1 = 2 + 10j
print('Real number: ',g1.real) 
print('imaginary number: ',g1.imag) 

(gx,gx1)=10, 2
print(gx**gx1) # ** stands for to the power

print(complex(2,9))  # complex number a+bj



largeNum = [10,234,654,23,323]
print('the large number is: ',max(largeNum))
print('the small number: ',min(largeNum))

############################### math libary
import math
print('aqrt of 144 is: ',math.sqrt(144))
print('value of pi:' ,math.pi)
print('value of e:' ,math.e)

########################################## lists
xL = [51,84,65,89,77,25,98,45]
yL = ['df','tt',98,8j, 'rt6']
print(xL,yL[3])
print(max(xL))
print("In reverse order: ",xL[::-1])
print(xL)
print("2nd elements",xL[::2]) #all the 2nd elements
print('2nd elements',xL[1::2])  #all the 2nd elements


print(xL + yL)  #merging list
aStr = list('hello how are you')  
print(aStr)
newlist = ['x']*10
print((newlist))

######################################### matrix

matrix = [[1,5,6],['a','b','c']]
print(matrix)

####################################### user input
firstName = input("enter your first name: ")
lastName = input("enter your last name: ")

print("your full name is: ",firstName,lastName)

numX = float(input("enter a number: "))
numY = float(input("enter another number: "))
print(numX+numY)
