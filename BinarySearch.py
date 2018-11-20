def binarySearch(searchList, searchNum):
    '''二分查找python实现'''
    low = 0
    height = len(searchList) -  1

    while low <= height:
        mid = (low + height) // 2
        if searchNum == searchList[mid]:
            return mid, True
        elif searchNum > searchList[mid]:
            low = mid + 1
        else:
            height = mid - 1
    return -1, False

if __name__ == '__main__':
    '''测试算法的正确性'''
    list = [3, 7, 8, 44, 58, 72, 98, 101]
    searchNum = 50
    location, flag = binarySearch(list, searchNum)
    if flag:
        print("Success!The location is:" + str(location))
    else:
        print("Failed.")