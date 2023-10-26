nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def bubbleSort(list):
    n=0
    l = 1
    for n in range(len(list)-1):
        while n < len(list)-l:
            if list[n] > list[n+1]:
                (list[n], list[n+1]) = (list[n+1], list[n])
            n+=1
        l +=1


bubbleSort(nums)
print(nums)
bubbleSort(words)
print(words)
