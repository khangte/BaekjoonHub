import sys
sys.setrecursionlimit(10000)

def dfs(airport, graph, route):
    while graph[airport]:
        next_airport = graph[airport].pop(0)
        dfs(next_airport, graph, route)
    route.append(airport)
        
def solution(tickets):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for src, dst in sorted(tickets):
        graph[src].append(dst)
        
    route = []
    
    dfs("ICN", graph, route)
    return route[::-1]