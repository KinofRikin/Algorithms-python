def findSmallest(arr):
    '''找出数组中最小的数，返回索引值'''
    smallest = arr[0]
    smallestIndex = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    '''选择排序的python实现'''
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)
        #注意pop的用法
        newArr.append(arr.pop(smallestIndex))
    return newArr

if __name__ == '__main__':
    '''测试用例'''
    testArr = [3, 33, 54, 28, 42, 10, 32]
    print("Test arr:")
    print(testArr)
    print("\n")
    sortedArr = selectionSort(testArr)
    print("After sort:")
    print(sortedArr)
    print("\n")
