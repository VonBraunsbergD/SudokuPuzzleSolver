""""
puzzle = [
    ['_','_','_','_','_','_','_','_','_'],
    ['_', 3 ,'_','_','_', 9 ,'_', 5 ,'_'],
    ['_','_', 9 , 8 , 2 ,'_','_', 1 , 3 ],
    [ 1 ,'_', 7 ,'_', 9 ,'_','_','_','_'],
    [ 3 ,'_','_','_','_','_','_', 4 , 5 ],
    ['_','_','_','_','_','_','_','_', 6 ],
    ['_', 2 ,'_','_', 7 , 4 ,'_','_','_'],
    ['_','_','_', 9 ,'_','_','_','_','_'],
    ['_', 6 ,'_', 1 ,'_', 5 , 4 ,'_','_']
]
"""
def solve(suku):
    find = find_empty(suku)                             # Base case for recursion
    if not find:                                        # If no empty spaces remain, base case met
        return True
    else:
        row, col = find                                 # If a value is returned
    for i in range(1, 10):                              # Loop through values 1 through 9
        if valid(suku, i, (row, col)):                  # If the number is valid...
            suku[row][col] = i                          # Fill that square with a number

            if solve(suku):                             # Call function again recursively
                return True                             # Puzzle is solved, return True
            
            suku[row][col] = "_"                        # Reset previously added number if i isn't valid

    return False                                        # If i is not valid, backtrack and try again

def valid(suku, num, pos):
    # Row
    for i in range(len(suku[0])):                       # Check that same number doesn't appear twice per row
        if suku[pos[0]][i] == num and pos[1] != i:      # Check to see if equal to number previously added
            return False                                # If duplicate found return False
        
    # Column
    for i in range(len(suku)):                          # Check that same number doesn't appear twice per column
        if suku[i][pos[1]] == num and pos[0] != i:
            return False

    # Box
    box_x = pos[1] // 3                                 # Use floor divison to create matrix
    box_y = pos[0] // 3                                 # [0,0] = Top left box [2,1] = Bottom center box etc...

    for y in range(box_y * 3, box_y * 3 + 3):           # Multiply by 3 to get the correct 'box' (0, 1, or 2)
        for x in range(box_x * 3, box_x * 3 + 3):       # Add 3 to include the correct indices in said box
            if suku[y][x] == num and (y, x) != pos:     
                return False
    
    return True                                         # If everything is valid, return True


def print_puzzle(suku):
    for y in range(len(suku)):                          # Count Y axis
        if y % 3 == 0 and y != 0:
            print("-----------------------")

        for x in range(len(suku[0])):                   # Count X Axis
            if x % 3 == 0 and x != 0:
                print(" | ", end="")                    # Print '|' line after every 3rd number w/o \n

            if x == 8:                                  # Insert sudoku numbers at the end of each row iteration
                print(suku[y][x])
            else:
                print(str(suku[y][x]) + " ", end="")    # Print numbers on same line with string concantenation


def find_empty(suku):                                   # Search for 'empty' squares in the puzzle
    for x in range(len(suku)):                          # Iterate through the rows
        for y in range(len(suku[0])):                   # Iterate through the columns
            if suku[x][y] == "_":                       # '_' == empty square
                return (x, y)                           # Return empty squares

    return None                                         # If no empty squares remain


#print_puzzle(puzzle)
#solve(puzzle)
#print("\n")
#print_puzzle(puzzle)