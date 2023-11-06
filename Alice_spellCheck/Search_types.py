def linearsearch(array,item):
    for data in range(len(array)):
        if item == array[data]:
            return data
    return -1

def binarySearch(list,data):
    lowerindex = 0
    upperindex = len(list)-1
    while lowerindex <= upperindex:
        index = (lowerindex + upperindex)//2
        if list[index] < data:
            lowerindex = index + 1
        elif list[index] > data:
            upperindex = index - 1
        else:
            return index
    return -1

