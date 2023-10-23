nums = [10, 30, 40, 45, 70, 80, 85, 90, 100]
words = ["at", "ball", "cat", "dog", "eye", "fish", "good"]
unsorted = [30, 20, 70, 40, 50, 100, 90]

def binarySearch(list,data):
    lowerindex = 0
    upperindex = len(list)
    while lowerindex <= upperindex:
        index = (lowerindex + upperindex)//2
        if list[index] < data:
            lowerindex = index + 1
        elif list[index] > data:
            upperindex = index - 1
            
        else:
            return index
    
    return -1




print(binarySearch(nums, 100))
print(binarySearch(nums, 75))
print(binarySearch(words, "fish"))
print(binarySearch(words, "at"))
print(binarySearch(unsorted, 70))
