#-----------------------------------list punctions
num = [10,20,30,25,40,35,50,60]
num2 = [80,90,100]

num.append(70)
print(num)

num.extend(num2)
print(num)

num.sort()
print(num)

num.insert(0, 5)
print(num)

num2.reverse()
print(num2)

num2.pop(2)
print(num2)

num.__add__(num2)
print('adding',num)

print(num2.__sizeof__())
print(len(num))
print(len(num2))

print('average: ',sum(num)//len(num))

#------------------------------------nest tuples
t1 = (1,42,35,447,5)
t2 = (10,20,20,20,30,40)
t3 = (t1,t2)
print(t3)
print(t1[::-1])

print(t2.count(20))
del t1 #---delets tuple

#-----------------------------------list to tuple and tuple to list
listX = [10,65,48,36,75,95,44]
print(type(listX))

tupleX = tuple(listX)
print(tupleX) 
print(type(tupleX))

listI = list(tupleX)
print(listI)
print(type(listI))

#------------------------------------nested tuple in list
nest = [('a','b','c'),(1,5,7)]
nest.append(('abc','def','ghi'))
print(nest)

nest.extend(('xyz','wxy', 'uvw'))
print(nest)

#------------------------------------nestd list in tuple

tpl = (['A','B','C'],['E','F','G'])
print(tpl)

tpl[0].append('D')
tpl[1].extend(('I','J'))
print(tpl)

#--------------------------------------for loop
for i in range(1, 10, 2):
    print(i)

for i in range(1, 11):
    print('loop' , i ,' : ', i)

z = [10,20,50,87,99]
for i in range(len(z)):
    print('list',i,' : ',z[i])   

#--------------------------------------if else with for loop
print("")
for i in range(0, 21, 1):
    if i == 0:
        print('Zero: ', i)
    elif i%2 == 0:
        print('Even: ', i)
    else:
        print('Odd: ', i) 
#-------------------------------------prime number
print('')
co=0
print('Prime: ')
for num in range(1, 101):
    c=0
    for i in range(2,num):
        if num%i == 0:
            c+=1
            
    if c==0:
        print(num,end=' ') 
        co+=1
print('how many prime number: ',co)  
#-------------------------------------functions
print("")
f1 = float(input('f1: '))
f2 = float(input('f2: '))

def function(f1,f2):
    sum = f1 + f2
    return sum

print(function(f1,f2))

#--------------------------------------string split
sp = "Welcome to Dhaka"
print(sp.split(" "))
