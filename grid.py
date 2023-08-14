# Grid layout
maze_grid=[
    ['B', '-', '-', '-', '-', 'F'],
    ['-', '-', '-', '-', 'B', '-'],
    ['-', '-', '-', 'F', '-', '-'],
    ['-', 'F', '-', '-', '-', '-'],
    ['-', 'B', '-', '-', '-', 'B'],
    ['-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-']
]
#Possible paths in the above maze given in the format of EWNS
maze_paths = {
    #(Row,column):(E,W,N,S)
    (0, 0): (1, 0, 0, 1), # From cell (0,0) possible and valid paths would be to east and south, i.e; (0,1) and (1,0)
    (1, 0): (0, 0, 1, 1),
    (2, 0): (0, 0, 1, 1),
    (3, 0): (1, 0, 1, 1),
    (4, 0): (0, 0, 1, 1),
    (5, 0): (0, 0, 1, 0),
    (6, 0): (1, 0, 0, 0),
    (0, 1): (1, 1, 0, 0),
    (1, 1): (0, 0, 0, 1),
    (2, 1): (1, 0, 1, 0),
    (3, 1): (0, 1, 0, 0),
    (4, 1): (1, 0, 0, 1),
    (5, 1): (1, 0, 1, 1),
    (6, 1): (0, 1, 1, 0),
    (0, 2): (0, 1, 0, 1),
    (1, 2): (1, 0, 1, 1),
    (2, 2): (0, 1, 1, 1),
    (3, 2): (0, 0, 1, 1),
    (4, 2): (1, 1, 1, 0),
    (5, 2): (1, 1, 0, 0),
    (6, 2): (1, 0, 0, 0),
    (0, 3): (1, 0, 0, 0),
    (1, 3): (1, 1, 0, 0),
    (2, 3): (1, 0, 0, 0),
    (3, 3): (1, 0, 0, 1),
    (4, 3): (1, 1, 1, 0),
    (5, 3): (0, 1, 0, 1),
    (6, 3): (1, 1, 1, 0),
    (0, 4): (1, 1, 0, 0),
    (1, 4): (0, 1, 0, 1),
    (2, 4): (1, 1, 1, 0),
    (3, 4): (1, 1, 0, 0),
    (4, 4): (1, 1, 0, 1),
    (5, 4): (0, 0, 1, 1),
    (6, 4): (0, 1, 1, 0),
    (0, 5): (0, 1, 0, 1),
    (1, 5): (0, 0, 1, 1),
    (2, 5): (0, 1, 1, 1),
    (3, 5): (0, 1, 1, 0),
    (4, 5): (0, 1, 0, 1),
    (5, 5): (0, 0, 1, 1),
    (6, 5): (0, 0, 1, 0),
}