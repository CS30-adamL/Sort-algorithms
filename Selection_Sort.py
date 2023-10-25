nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def SelectionSort(list):
        n=0
        for n in range(n,len(list)-1):
            minimum = min(list[n:len(list)])
            pos = list.index(minimum)
            if list[n] > minimum:
                    first_ele = list[n]
                    second_ele = list[pos]
                    del list[n]
                    del list[pos-1]
                    list.insert(n,second_ele)
                    list.insert(pos,first_ele)
                    n+=1
            n+=1

# SelectionSort(nums)
# print(nums)
# SelectionSort(words)
array = [5, 4, 3, 2, 1]
SelectionSort(array)
print(array)
# print(words)
