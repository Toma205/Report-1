import random

def generate_grid(n):
    return [[random.choice([0, 1]) for _ in range(n)] for _ in range(n)]

def get_random_non_obstacle(grid):
    n = len(grid)
    while True:
        x, y = random.randint(0, n-1), random.randint(0, n-1)
        if grid[x][y] == 0:
            return (x, y)

def dfs(grid, source, goal):
    n = len(grid)
    stack = [source]
    parent = {source: None}
    visited = set()
    topological_order = []
    moves = []
    directions = {(-1, 0): "Up", (1, 0): "Down", (0, -1): "Left", (0, 1): "Right"}
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        topological_order.append(node)
        
        if node == goal:
            break
        
        x, y = node
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        random.shuffle(neighbors)
        
        for nx, ny in neighbors:
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = node
                moves.append(f"Moving {directions.get((nx-x, ny-y), '?')} ({nx}, {ny})")
    
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    
    if path and path[0] != source:
        path = []
    
    return path, topological_order, moves

def print_grid(grid):
    print("The graph :")
    for row in grid:
        print(row)

def main():
    n = random.randint(4, 7)
    grid = generate_grid(n)
    
    source = get_random_non_obstacle(grid)
    goal = get_random_non_obstacle(grid)
    while goal == source:
        goal = get_random_non_obstacle(grid)
    
    path, topological_order, moves = dfs(grid, source, goal)
    
    print(f"The Grid size : {n}")
    print_grid(grid)
    print(f"\nRandom source x {source[0]}")
    print(f"Random source y {source[1]}")
    print(f"Random goal x {goal[0]}")
    print(f"Random goal y {goal[1]}\n")
    
    if path:
        for move in moves:
            print(move)
        print("\nGoal found")
        print(f"Number of moves required = {len(path) - 1}")
    else:
        print("No path found")
    
    print(f"Topological Order: {topological_order}")

if _name_ == "_main_":
    main()