# Function that takes a list and target parameter
def binary_search(list, element):

# multiple variable; middle, start, end, steps
    middle = 0
    start = 0
    end = len(list)
    steps = 0

# recursion or while loop / # increase the steps each time a split is done
    while(start <= end):
        print('Step', steps, ':',str(list[start:end + 1]))

        steps = steps + 1
        middle = (start + end) // 2

# conditions to track target positions
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1        

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
target = 14
binary_search(my_list, target)