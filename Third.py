#---------------------------------Dictionary
dic = {'name':('waliul', 'hasan','iram'), 'age': 23, 'prof': 'student'}
print(dic)

dic['prof'] = {'CSE Student'}  #updating dictionary
print(dic)

print(dic['name'])      #accessing data with key
print(dic.get('age'))

key = {'a','b','c','d','e'}; value = {1,24,36,47,5}
print(dict.fromkeys(key,value))

#-----------------------------------sets
s1=set([1,3,5,6,9]); s3=set([1,3,5])
s2=set([2,5,6,9,8])

print('set1 and set2: ',s1,s2)

test1 = s1.union(s2)            #union
test2 = s1.intersection(s2)     #intersection
print('Union: ',test1)
print('Intersection: ',test2)

test3 = s1.issuperset(s3)       #supperset
test4 = s1.issubset(s3)
print(test3)

#----------------------------------------while loop
In = float(input("Enter a number: "))
def multipul(In):
    while In % 5 != 0:
        print("%d is not a mutipul of 5" %In)
        In = float(input("Enter a number: "))
    else:
        print("%d is a multipul of 5" %In)    

multipul(In)
#-------------------------------------------matrix with while loop
mat = [[1,2,4], [4,5,7],[8,9,6]]
for i in mat:
    for j in i:
        print(j, end=" ")
    print('')    
#---------------------------------------------reverse number
n = int(input("Enter a number: ")) 
nr = 0
while n%10 != 0:
    c = n%10
    nr = nr*10 + c
    n = n//10
print("Reverse number: %d"%nr)   
#--------------------------------------length without len functioc
l = [1,23,4,"hello"]
length = 0
i = 0
try:
    while l[i]:
        length+=1
        i+=1
except:
       print("length of the list is: %d" %length)

#--------------------------------------------------pattern      
enter = int(input("Enter a number: "))
i = 1
while i <= enter:
    j = 1
    while j <= i:
        print(j,end=' ')
        j+=1
    i+=1
    print()  

while i>=1:
    j = i
    while j>=1:
        print(i-j,end=' ')
        j=j-1
    i=i-1  
    print()
#------------------------------------------guessing game
import random
nump = random.randint(100, 999) 
print(nump)
n = int(input("Enter a number: "))

while n != 10:
    num = nump
    cor = 0

    while num % 10:
        numc = num %10
        nc = n %10
        num = num // 10
        n = n // 10 
        if numc == nc:
            cor = cor + 1    
    if cor == 3:
        print("Cogratulations, you win, got all the numbers")
        break

    else:
        print("%d number the at the right position" %cor)
        n = int(input("Enter a number: "))           
else:
    print("you quit the game")

 #----------------------------------------- Array
from array import *
arr = array('i', [1,45,3,69,8])
print(arr)
print("the address & the size",arr.buffer_info()) 

for i in range(len(arr)):
    print(arr[i], end=" ")
print()    
for i in arr:
    print(i, end=" ")
print()

for i in range(1,4):
    print(arr[i], end=" ")

print()

arr.reverse()
print(arr)
arr.reverse()
print(arr)

for i in arr:
    print(i, end=" ")
print() 
#------------------------------------user-input of array
arra = ['i' ,[]]
size = int(input("Enter the size of the array: "))
print("Enter %d elements" %size)

for i in range(size):
    enp = int(input())
    arra.append(enp)
print("elements of the array: ")
for i in range(len(arra)):
    print(arra[i])    
       
#----------------------------------------array 
def array(it):
    qr = ['i', []]
    print("enter %d elements: " %it)
    for i in range(it):
        elem = int(input())
        qr.append(elem)
    print("the elements of the array are: ")
    for i in qr:
        print(i, end=" ")     

it = int(input("Enter the size of the array: "))
array(it)
