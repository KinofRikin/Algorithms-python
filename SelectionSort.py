def selectionSort(sortList):
    '''选择排序的python实现'''
    for i in range(len(sortList)):
        Max = 0
        for j in range(len(sortList)-i):
            print(j)
            if sortList[j] > Max:
                Max = sortList[j]
                #print(j)
        print(Max)
        k = 0
        while True:
            if sortList[k] == Max:
                break
            else:
                k = k + 1

        temp = sortList[len(sortList)-i-1]
        sortList[len(sortList)-i-1] = Max
        sortList[k] = temp
        #print(Max)
        print(sortList)
    return sortList

if __name__ == '__main__':
    '''测试用例'''
    sortList = [3, 72, 5, 17, 18, 52, 23]
    sortedList = selectionSort(sortList)
    print("\n")
    print("Before:")
    print(sortedList)
