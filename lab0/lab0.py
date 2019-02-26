f = open('lab0_for_Python.txt', 'r') #открытие на чтение
lst = []
for a in f:
    lst.sort()
    lst.append(int(a)) #цифры, а не текст
    maximum = max(lst)
    minimum = min(lst)
    print("")
    print (str(minimum) + "-" + str(maximum))
        
    if maximum - minimum != len(lst)-1:
        print("Not all messages received")
        print("Not enough:")
        for i in range(minimum + 1, maximum):
            for j in range(0, len(lst)):
                if i == lst[j]:
                    break
                if i < lst[j]:
                    print (i)
                    break      
    else:
        print("All messages received")
    
                   