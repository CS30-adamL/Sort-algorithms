# nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
# words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

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





# SelectionSort(nums)
# print(nums)
# SelectionSort(words)
# print(words)

# selectionSort(nums) 
# selectionSort(words) 
# print(nums) 
# print(words)