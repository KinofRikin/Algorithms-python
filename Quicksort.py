def quickSort(list):
    '''快速排序python实现'''
    if len(list) < 2:
        return list
    else:
        baseValue = list[0]
        smallerList = [i for i in list[1:] if i < baseValue]
        largerList = [i for i in list[1:] if i > baseValue]
        return quickSort(smallerList) + [baseValue] + quickSort(largerList)

if __name__ == '__main__':
    '''测试案例'''
    list = [3,55,40,21,1,93,22]
    print("Before sort:")
    print(list)
    print("\n")
    sortedList = quickSort(list)
    print("After sort:")
    print(sortedList)
    print("\n")
