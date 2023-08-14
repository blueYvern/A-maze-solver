from grid import maze_grid,maze_paths
from Astar import aStar


#Fetch dynamic inputs to determine start and the goal of the grid
def fetch_grid_endpoints(grid):
    rows,cols = len(grid),len(grid[0])
    start_x,start_y,goal_x,goal_y = float('-inf'),float('-inf'),float('-inf'),float('-inf')
    while True:
        try:
            print("Fetching the start and end points for the cave")
            print("Starting Point: ")
            start_x = int(input(f"Enter the row(Range: 0 to {rows - 1}): "))
            start_y = int(input(f"Enter the column(Range: 0 to {cols -1})):"))
            print("Goal Point: ")
            goal_x = int(input(f"Enter the row(Range: 0 to {rows - 1}): "))
            goal_y = int(input(f"Enter the column(Range: 0 to {cols -1})):"))

            if not (0 <= start_x < rows or 0 <= start_y < cols) or not (0 <= goal_x < rows or 0 <= goal_y < cols):
                raise ValueError()
            start = start_x,start_y
            goal = goal_x,goal_y
            return start,goal 
            break
        except ValueError:
            print(f"Entered input is invalid. Enter a valid row and column in the mentioned format")



####################################################
if __name__=='__main__':
    start,goal = fetch_grid_endpoints(maze_grid)
    #start,goal = (6,0),(6,4)

    astar_best_path, astar_best_cost = aStar(start,goal,maze_grid,maze_paths)

    if astar_best_path :
        print("-----------------A* Best Path:-----------------")
        cost =0
        for step,pos in enumerate(astar_best_path):
            print(f"Step {step+1}: {pos} Cost: {cost}",end="")
            row,col = pos
            if maze_grid[row][col] == 'B':
                print(f" (Bush)",end="")
                cost+=1
            elif maze_grid[row][col] == 'F':
                print(f" (Fire)",end="")
                cost+=5
            cost+=3
            print()
        print(f"----------------- A* Total Cost:{cost-3}-----------------")
    else:
        print("No valid path found to reach the goal")
