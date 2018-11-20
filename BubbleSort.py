def bubbleSort(sortList):
    '''冒泡排序的python实现代码'''
    for i in range(len(sortList)-1):
        for j in range(len(sortList)-i-1):
            if sortList[j] > sortList[j+1]:
                temp = sortList[j]
                sortList[j] = sortList[j+1]
                sortList[j+1] = temp
        print(sortList)
    return sortList

if __name__ == '__main__':
    '''测试用例'''
    sortList = [72, 71, 66, 55, 43, 32, 23]
    print("Before sort:")
    print(sortList)
    print("\n")
    sortedList = bubbleSort(sortList)
    print("\n")
    print("After sort:")
    print(sortedList)
