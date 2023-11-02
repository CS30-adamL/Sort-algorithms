# SORT ANALYZER STARTER CODE

import time
import Insertion_Sort
import Selection_Sort
import bubble_Sort
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
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

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


def sortspeed(list,type,creator):
    start_time = time.time()
    sort_type(type,list)
    end_time = time.time()
    total = end_time - start_time
    print(f'\nlist sorted with {creator} method: ({total} seconds)')
    return total

def sort_type(type,list):
    if type == 1:
        Selection_Sort.SelectionSort_My_Way(list)
    elif type == 2:
        Selection_Sort.SelectionSort_Normal_Way(list)

def percent_diff(list,list2):
    my_way = sortspeed(list,1,"MY")
    normal_way = sortspeed(list2,2,"NORMAL")
    percent = ((normal_way/my_way)*100)//1
    print(f"\nNormal_way:{normal_way} / My_way:{my_way} ={normal_way/my_way}, (~{percent}%)\nMy method is {percent/100} times faster than the normal way\n")
    return percent/100

array  = [6,7,3,8,5,2,9,4,1,4,5,4,8,5,2,7,3,8,5,2]
array2 = [6,7,3,8,5,2,9,4,1,4,5,4,8,5,2,7,3,8,5,2]
# percent_diff(list,list2)
# percent_diff(array,array2)

def Average():
    average = 0
    for _ in range(0,60):
        newlist = []
        newlist,newlist2 = make_rand_list(newlist)
        speed = percent_diff(newlist,newlist2)
        average += speed
    average = average/59
    return average

