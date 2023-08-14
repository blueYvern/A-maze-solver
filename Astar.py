from queue import PriorityQueue

#Fetches all of the possible paths for a cell in the maze grid as per the given maze path_map
def get_possible_paths(currCell,path_map):
    poss_paths = []
    if currCell in path_map:
        all_paths = path_map[currCell]

        if all_paths[0] == 1:
            poss_paths.append((currCell[0],currCell[1]+1))
        if all_paths[1] == 1:
            poss_paths.append((currCell[0],currCell[1]-1))
        if all_paths[2] == 1:
            poss_paths.append((currCell[0]-1,currCell[1]))
        if all_paths[3] == 1:
            poss_paths.append((currCell[0]+1,currCell[1]))

    return poss_paths


#Heuristic function (eg: Manhattan distance)
def heuristic(cell1, cell2):
    x1,y1 = cell1
    x2,y2 = cell2
    return (abs(x1-x2) + abs(y1-y2))

# To check the step cost when transitioning to the given cell   
def check_step_penalty(cell,grid):
    x,y = cell
    default_penalty = 0 #no penalty by default
    
    if grid[x][y] == 'B':
        return default_penalty + 1 # penalty of extra one step in case of Bush
    elif grid[x][y] == 'F':
        return default_penalty + 5 # penalty of extra 5 steps in case of fire
    else:
        return default_penalty

#A* Algorithm
def aStar(start,goal,maze_grid,path_map):
    rows, cols = len(maze_grid), len(maze_grid[0])
    visited_cells = set()
    open = PriorityQueue()
    # Use a priority queue with a tuple containing (total_cost + heuristic, current_cost, current_cell, path)
    open.put((0, 0, start, [start]))

    while not open.empty():
        total_cost, current_cost, currCell, path = open.get()
        
        if currCell in visited_cells:
            continue
            
        visited_cells.add(currCell)
        
        if currCell == goal:  # Goal check
            return path, total_cost

        for childCell in get_possible_paths(currCell,path_map):
            new_cost = current_cost + check_step_penalty(childCell,maze_grid)
            heuristic_cost = heuristic(childCell, goal)
            total_cost = new_cost + heuristic_cost
            new_path = path + [childCell]

            open.put((total_cost, new_cost, childCell, new_path))

    return [], float('inf')