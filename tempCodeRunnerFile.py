def array(it):
    qr = ['i', []]
    print("enter %d elements: " %it)
    for i in range(it):
        elem = int(input())
        qr.append(elem)
    print("the elements of the array are: ")
    for i in qr:
        print(i, end=" ")   
    m = 0
    for i in qr:
        if (i>m):
            m = i
    print("max value: ", m)   
it = int(input("Enter the size of the array: "))
array(it)
