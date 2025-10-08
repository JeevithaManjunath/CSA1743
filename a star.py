import heapq 
def astar(start, goal, neighbors_fn, heuristic_fn): 
    """ 
    Find the shortest path from start to goal using A* algorithm.
    Arguments: 
        start: the starting node 
        goal: the goal node 
        neighbors_fn: a function that takes a node and returns its neighbors 
        heuristic_fn: a function that takes a node and returns the estimated 
                      distance to the goal node 
    Returns: 
        A tuple containing the path from start to goal and its cost 
    """ 
    frontier = [] 
    heapq.heappush(frontier, (0, start)) 
    came_from = {} 
    cost_so_far = {} 
    came_from[start] = None 
    cost_so_far[start] = 0 
    while frontier: 
        _, current = heapq.heappop(frontier) 
        if current == goal: 
            break 
        for neighbor in neighbors_fn(current): 
            new_cost = cost_so_far[current] + 1 
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]: 
                cost_so_far[neighbor] = new_cost 
                priority = new_cost + heuristic_fn(neighbor, goal) 
                heapq.heappush(frontier, (priority, neighbor)) 
                came_from[neighbor] = current
              path = [goal] 
current = goal 
while current != start: 
current = came_from[current] 
path.append(current) 
path.reverse() 
