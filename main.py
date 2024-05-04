from state import State
from problem import Problem

def read_user_input(s):
    result = s.split(',')
    result = [int(x) for x in result]
    return result

def calcuate_misplaced_tiles(curr_state_rep, goal_state_rep):
    misplaced_count = 0
    for i in range(len(curr_state_rep)):
        for j in range(len(curr_state_rep)):
            if curr_state_rep[i][j] != goal_state_rep[i][j]:
                misplaced_count += 1
    return misplaced_count

def calcuate_euclidean_distance(curr_state,goal_state):
    return

def pythagorean(a, b, c, d):
    dista = a - c
    distb = b - d
    dista *= dista
    distb *= distb
    totalDist = dista + distb
    totalDist = totalDist ** 0.5
    return totalDist

def euclidean(rep):
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for n in range(3):
        for j in range(3):
            if rep[n][j] == 0:
                temp1 = 2
                temp2 = 2
                temp = pythagorean(n, j, 2, 2)
                res[n][j] = temp
            elif rep[n][j] == (n + 1) * (j + 1):
                continue
            else:
                temp = rep[n][j]
                temp1 = (temp - 1) % 3
                temp2 = (temp - 1) / 3
                temp = pythagorean(n, j, temp2, temp1)
                res[n][j] = temp
    return res

# def printEuclidean(rep):
#     res = euclidean(rep)
#     for i in range(3):
#         for j in range(3):
#             print(res[i][j])
            
# def print2D(rep):
#     for i in range(3):
#         for j in range(3):
#             print(rep[i][j])
                

s = State([0, 4, 2], [1, 8, 6], [5, 7, 3])
print(euclidean(s.state_rep))

print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")
option  = input( "Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
print(option)
if option == "1":
    start_state = State([1,2,3],[4,8,0],[7,6,5])
    print(start_state.state_rep)
# have a predetermined state asshown 
if option  == "2":
    print("Enter your puzzle, use a zero to represent the blank")
    first_row = input( "Enter the first row, use commas between numbers")
    second_row = input( "Enter the second row, use commas between numbers")
    third_row = input( "Enter the third row, use commas between numbers")
    first_row = read_user_input(first_row)
    second_row = read_user_input(second_row)
    third_row = read_user_input(third_row)
    start_state = State(first_row, second_row, third_row)
    print(start_state.state_rep)

algo = input("Enter your choice of algorithm:\n 1: Uniform Cost Search\n 2: A* with the Misplaced Tile heuristic\n 3: A* with the Euclidean Distance heuristic\n")

if algo == "1":
    # run uniform search here
    print("You ran Uniform Cost Search\n")
elif algo == "2":
    #run misplaced here
    print("You ran A* search with Misplaced Tile heuristic\n")
elif algo == "3":
    #run euclidean here
    print("You ran A* search with Euclidean Distance heuristic\n")
else:
    print("Input not recognized. Please input 1, 2, or 3.")