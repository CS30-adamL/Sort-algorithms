
def bubbleSort(list):
    for l in range(len(list)-1):
        for n in range(len(list) - 1 - l):
            if list[n] > list[n+1]:
                (list[n], list[n+1]) = (list[n+1], list[n])


def insertion_Sort(anArray):
    arraylength = len(anArray)
    for ele in range(1,arraylength):
        first_val = anArray[ele]
        move = ele - 1
        while move >= 0 and first_val < anArray[move]:
            anArray[move +1] = anArray[move]
            anArray[move] = first_val
            move -= 1


def SelectionSort_My_Way(list):
        n=0
        for n in range(n,len(list)-1):
            minimum = min(list[n:len(list)])
            pos = list.index(minimum,n,len(list))
            if list[n] > minimum:
                    (list[n], list[pos]) = (list[pos], list[n]) 
                    n+=1
            n+=1


#proper way
def SelectionSort_Normal_Way(anArray):
        arraysize = len(anArray) 
        for ind in range(arraysize): 
                minIndex = ind
                for j in range(ind+1,arraysize):
                        if anArray[j] < anArray[minIndex]: 
                                minIndex = j 
                (anArray[ind], anArray[minIndex]) = (anArray[minIndex], anArray[ind]) 

