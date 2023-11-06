# SORT ANALYZER STARTER CODE

import time
import SORT_METHODS
import random
# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("Sort-analyzer/data-files/random-values.txt")
reversedData = loadDataArray("Sort-analyzer/data-files/reversed-values.txt")
nearlySortedData = loadDataArray("Sort-analyzer/data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("Sort-analyzer/data-files/few-unique-values.txt")
array_types = [(randomData, "RandomData"),(reversedData,"ReversedData"),(nearlySortedData,"NearlySortedData"),(fewUniqueData,"FewUniqueData")]
sort_types = ["Selection Sort (normal way)","Bubble Sort","Insertion Sort","Selection Sort (my Way)"]

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
print(randomData[0:50])
print(reversedData[0:50])
print(nearlySortedData[0:50])
print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")

def sort_type(type,list):
    if type == "Selection Sort (my Way)":
       SORT_METHODS.SelectionSort_My_Way(list)
    elif type == "Selection Sort (normal way)":
        SORT_METHODS.SelectionSort_Normal_Way(list)
    elif type == "Bubble Sort":
        SORT_METHODS.bubbleSort(list)
    elif type == "Insertion Sort":
        SORT_METHODS.insertion_Sort(list)

def sortspeed(list,type):
    start_time = time.time()
    sort_type(type,list)
    end_time = time.time()
    total = end_time - start_time
    # print(f'list sorted with {type} method: ({total} seconds)')
    return total

def Average(array,Sort_type):
    average = 0
    reps = 5
    for _ in range(0,reps):
        
        copy = array[0].copy()
        speed = sortspeed(copy,Sort_type)
        average += speed
    average = average/reps
    print(f"The average speed of {Sort_type}: {average} || Array Type: {array[1]}")
    return (type,average) 

for type in sort_types:
    print("")
    for array in array_types:
        Average(array,type)
    
