import queue

def breadthFirstSearch(graph, name, item):
    '''广度优先搜索python实现'''
    searchQueue = queue.Queue()
    '''18/12/01更新，添加了lenMap字典以记录路径长度'''
    lenMap = {}
    for graphName in graph[name]:
        lenMap[graphName] = 1
        searchQueue.put(graphName)

    searched = []

    while searchQueue:
        queueItem = searchQueue.get()
        if queueItem not in searched:
            if queueItem == item:
                return lenMap[queueItem]
            else:
                for itemName in graph[queueItem]:
                    if itemName not in lenMap.keys():
                        lenMap[itemName] = lenMap[queueItem] + 1

                    searchQueue.put(itemName)

                searched.append(queueItem)
        else:
            pass
    return -1

if __name__ == '__main__':
    '''测试用例'''
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = ["test"]
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    length = breadthFirstSearch(graph, "you", "test")
    print(length)

