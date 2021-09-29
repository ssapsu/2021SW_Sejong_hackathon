import queue

graph = {}
infinity = float("inf")
cost = {}
parents = {}
processed = []
# 오현수 입니다.

# 초기화 
def init(): 
    global graph, infinity, costs, parents, processed 
    graph = {} # 간선 정보 입력 
    graph["A"] = {} 
    graph["A"]["B"] = 5 
    graph["A"]["C"] = 0 
    graph["B"] = {} 
    graph["B"]["D"] = 15 
    graph["B"]["E"] = 20 
    graph["C"] = {} 
    graph["C"]["D"] = 30 
    graph["C"]["E"] = 35 
    graph["D"] = {}
    graph["D"]["F"] = 20 
    graph["E"] = {} 
    graph["E"]["F"] = 10 
    graph["F"] = {} 
    # ---------------------------------------- 
    infinity = float("inf") 
    # ------------------------------------------ 
    costs = {} # 해당 노드 최단경로 입력 
    costs["A"] = infinity 
    costs["B"] = infinity 
    costs["C"] = infinity 
    costs["D"] = infinity 
    costs["E"] = infinity 
    costs["F"] = infinity 
    # ------------------------------------------- 
    # parents = {} # 추적 경로를 위해 부모 설정 
    parents["B"] = None 
    parents["C"] = None 
    parents["D"] = None 
    parents["E"] = None 
    parents["F"] = None 
    # ------------------------------------------- 
    processed = []

출처: https://www.crocus.co.kr/1688 [Crocus]


def find_lowest_cost_node(costs): 
    lowest_cost = float("inf") 
    lowest_cost_node = None
    for node in costs: 
        cost = costs[node] 
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node

# 다익스트라 알고리즘 
def dijkstra(graph, start, final): 
    node = start 
    costs[start] = 0 
    while node is not None: 
        cost = costs[node] 
        neighbors = graph[node] 
        for n in neighbors.keys(): 
            new_cost = cost + neighbors[n] 
            if costs[n] > new_cost: # 현재 가지고있는 cost보다 new_cost가 더 최단거리라면 
                costs[n] = new_cost # 갱신 
                parents[n] = node 
                processed.append(node) 
                node = find_lowest_cost_node(costs) # 경로 추적 로직 
    trace = [] 
    current = final 
    while current != start: 
        trace.append(current) 
        current = parents[current] 
        trace.append(start) 
        trace.reverse() 
        print("=== Dijkstra ===") 
        print(start, "에서 ", final, "까지의 정보") 
        print("최단 거리 : ", costs[final]) 
        print("진행 과정 : ", processed) 
        print("경로 : ", trace)
