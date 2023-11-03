# nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
# words = ["dog","at", "good", "eye", "cat", "ball", "fish"]



def insertion_Sort(anArray):
    arraylength = len(anArray)
    for ele in range(1,arraylength):
        first_val = anArray[ele]
        move = ele - 1
        while move >= 0 and first_val < anArray[move]:
            anArray[move +1] = anArray[move]
            anArray[move] = first_val
            move -= 1


# insertion_Sort(nums)
# insertion_Sort(words)

# print(nums)
# print(words)