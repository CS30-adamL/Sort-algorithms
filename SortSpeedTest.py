import time
import Selection_Sort
list = []

def sortspeed(list):
    start_time = time.time()

    sort = sort_type(input("1 or 2"),list)
    end_time = time.time()
    total = end_time - start_time
    print(f"list sorted: {sort}.    ({total} seconds)")


def sort_type(type,list):
    if type == 1:
        Selection_Sort.SelectionSort(list)
    elif type == 2:
        Selection_Sort.selectionSort(list)
