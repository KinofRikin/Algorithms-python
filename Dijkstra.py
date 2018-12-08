def findLowestCostNode(costs, processed):
    lowestCost = float('inf')
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

def dijkstra(graph, costs, parents, begin, end):
    '''dijkstra算法python实现，注意，该算法只适用于有向无环图'''
    '''算法要点：
       ①找出可在最短时间内前往的节点；
       ②对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销；
       ③重复①②过程，直到所有的节点被检查完毕；
       ④得出最终路径；'''
    processed = []

    node = findLowestCostNode(costs[begin], processed)
    while node is not None:
        cost = costs[begin][node]
        neighbors = graph[node]
        for n in neighbors.keys():
            newCost = cost + neighbors[n]
            if costs[begin][n] > newCost:
                costs[begin][n] = newCost
                parents[n] = node
        processed.append(node)
        node = findLowestCostNode(costs[begin], processed)

    return costs[begin][end]

if __name__ == '__main__':
    '''测试用例'''
    graph = {}

    #graph init
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    graph["fin"] = {}

    #cost init
    infinity = float("inf")
    costs = {}
    #costs字典内可以添加任意多的节点，此处只以最简单情况作为考量
    costs["start"] = {}
    costs["start"]["a"] = 6
    costs["start"]["b"] = 2
    costs["start"]["fin"] = infinity

    #parent init
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    #test begin
    lowestCost = dijkstra(graph, costs, parents, "start", "fin")
    print("The lowest cost is:")
    print(lowestCost)