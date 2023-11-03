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
array_types = [randomData,reversedData,nearlySortedData,fewUniqueData]
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

def Average(array,type):
    average = 0
    reps = 5
    for _ in range(0,reps):
        
        copy = array.copy()
        speed = sortspeed(copy,type)
        average += speed
    average = average/reps
    print(f"\nThe average speed of {type}: {average} || Array Type: {}")
    return (type,average) 

for type in sort_types:
    for array in array_types:
        Average(array,type)


def percent_diff(array,type1,type2):
    list1 = array
    list2 = array
    method1 = sortspeed(list1,type1)
    method2 = sortspeed(list2,type2)
    percent = ((method1/method2)*100)//1
    print(f"\nMethod 1:{method1} / Method 2:{method2} ={method1/method2}, (~{percent}%)\nMethod 1 is {percent/100} times faster than Method 2.\n")
    return percent/100

# def Average():
#     average = 0
#     for _ in range(0,60):
#         newlist = []
#         newlist,newlist2 = make_rand_list(newlist)
#         speed = percent_diff(newlist,newlist2)
#         average += speed
#     average = average/59
#     return average



def make_rand_list(newlist):
    
    for num in range(0,1001):
        randval = random.randrange(0,1000)
        newlist.append(randval)
    newlist2 = newlist.copy()
    return newlist,newlist2
