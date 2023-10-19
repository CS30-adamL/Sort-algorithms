nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

# def bubbleSort(list):
#     i = 0
#     while i < len(list):
#         n=i
#         while n < len(list):
#             print(list[i],list[n])
#             if list[i] > list[n]:
#                 list.insert(i,list[n])
#                 list.insert(n,list[i])
#                 print(list)
#                 n +=1
            
#         i +=1

def bubbleSort(list):
    f=0
    n=f+1
    while f < len(list):
        while n <= len(list):
            print(list[f],list[n])
            if list[n-1] > list[n]:
                    first_ele = list[n-1]
                    second_ele = list[n]
                    del list[n-1]
                    del list[n]
                    # inserting in each others positions
                    list.insert(n-1,second_ele)
                    list.insert(n,first_ele)
                    n+=1
            f+=1
            
        



bubbleSort(nums)
print(nums)
bubbleSort(words)



print(words)
