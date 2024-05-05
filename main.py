from state import State
from problem import Problem

def read_user_input(s):
    result = s.split(',')
    result = [int(x) for x in result]
    return result

def misplaced_tiles(curr_state_rep, goal_state_rep):
    misplaced_count = 0
    for i in range(len(curr_state_rep)):
        for j in range(len(curr_state_rep)):
            if curr_state_rep[i][j] != goal_state_rep[i][j]:
                misplaced_count += 1
    return misplaced_count

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

def Astar_with_misplaced_tiles(problem):
    node_count = 0
    max_in_queue = 0
    frontier = [problem.start_state]
    explored = []
    failure = False
    while failure == False:
        if len(frontier) == 0:
            failure = True
            print("Couldn't solve puzzle")
            break
        curr_state = frontier.pop(0)
        curr_state.set_h(misplaced_tiles(curr_state.state_rep, problem.goal_state))
        print(f"The best state to expand with {curr_state.f} and {curr_state.h} is ")
        curr_state.print_state_rep()
        node_count += 1
        if curr_state.state_rep == problem.goal_state:
            print("Reached Goal State")
            print(f"To solve this problem the search algorithm expanded a total of {node_count} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {max_in_queue}")
            print(f"The depth of the goal node was {curr_state.g}nodes.")
            break
        else:
            explored.append(curr_state)
            curr_state.get_next_states()
            nextStates = curr_state.next_states
            for state in nextStates:
                state.h = misplaced_tiles(state.state_rep, problem.goal_state)
                state.get_f()
            for state in nextStates:
                for exploredState in explored:
                    if(compare_two_states(state, exploredState) == False):
                        frontier.append(state)
            if len(frontier) > max_in_queue:
                maxInQueue = len(frontier)
            sortStates(frontier)
    return

def totalEuclidean(rep):
    res = euclidean(rep)
    total = 0
    for i in range(3):
        for j in range(3):
            total += res[i][j]
    return total
    
# def printEuclidean(rep):
#     res = euclidean(rep)
#     for i in range(3):
#         for j in range(3):
#             print(res[i][j])
            
# def print2D(rep):
#     for i in range(3):
#         for j in range(3):
#             print(rep[i][j])
                
def sortStates(frontier):
    for j in range(len(frontier)):
        min = j
        for i in range(j + 1, len(frontier)):
            temp = i
            if(frontier[min].f > frontier[temp].f):
                min = temp
        temp1 = frontier[min]
        frontier[min] = frontier[j]
        frontier[j] = temp1
        
def compare_two_states(state1,state2):
    if state1.state_rep == state2.state_rep and state1.g == state2.g and state1.h == state2.h:
        return True
    return False

def aStarEuclidean(problem):
    nodeCount = 0
    maxInQueue = 0
    frontier = [problem.start_state]
    explored = []
    failure = False
    while failure == False:
        if len(frontier) == 0:
            failure = True
            print("Couldn't solve puzzle")  
            break
        curr_state = frontier.pop(0)
        print(f"The best state to expand with {curr_state.g} and {curr_state.h} is ")
        curr_state.print_state_rep()
        nodeCount += 1
        if curr_state.state_rep == problem.goal_state:
            print("Reached Goal State")
            print(f"To solve this problem the search algorithm expanded a total of {nodeCount} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {maxInQueue}")
            print(f"The depth of the goal node was {curr_state.g}.")
            break
        else:
            explored.append(curr_state)
            curr_state.get_next_states()
            nextStates = curr_state.next_states
            for state in nextStates:
                state.h = totalEuclidean(state.state_rep)
                state.get_f()
            for state in nextStates:
                for exploredState in explored:
                    if(compare_two_states(state, exploredState) == False):
                        frontier.append(state)
            if len(frontier) > maxInQueue:
                maxInQueue = len(frontier)
            sortStates(frontier)
                

                
def uniformCostSearch(problem):
    nodeCount = 0
    maxInQueue = 0
    frontier = [problem.start_state]
    explored = []
    failure = False
    while failure == False:
        #print("Length of frontier", len(frontier))
        if(len(frontier) == 0):
            failure = True
            print("Couldn't solve")
            break
        curr_node = frontier.pop(0)
        nodeCount += 1
        print(f"The best state to expand with {curr_node.g} is ")
        curr_node.print_state_rep()
        if curr_node.state_rep == problem.goal_state:
            print("Reached Goal State")
            print(f"To solve this problem the search algorithm expanded a total of {nodeCount} nodes.")
            print(f"The maximum number of nodes in the queue at any one time: {maxInQueue}")
            print(f"The depth of the goal node was {curr_node.g}.")
            break 
        explored.append(curr_node)
        curr_node.get_next_states()
        nextStates = curr_node.next_states
        #print("Nextstates: ", len(nextStates))
        for states in nextStates:
            frontier.append(states)
            #print("Length after append: ", len(frontier))
        if len(frontier) > maxInQueue:
            maxInQueue = len(frontier)
            
s = State([1,2,0],[4, 5, 3],[7, 8, 6])
p = Problem(s)
Astar_with_misplaced_tiles(p)

# s = State([0, 4, 2], [1, 8, 6], [5, 7, 3])
# print(euclidean(s.state_rep))

print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")
# just add a while loop in case they type 3 or some other stuff
option  = input( "Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n")
print(option)
if option == "1":
    start_state = State([1,2,3],[4,8,0],[7,6,5])
    print(start_state.state_rep)
# have a predetermined state as shown 
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
problem = Problem(start_state)
algo = input("Enter your choice of algorithm:\n 1: Uniform Cost Search\n 2: A* with the Misplaced Tile heuristic\n 3: A* with the Euclidean Distance heuristic\n")

if algo == "1":
    # run uniform search here
    print("You ran Uniform Cost Search\n")
elif algo == "2":
    #run misplaced here
    problem.start_state.h = misplaced_tiles(problem.start_state,problem.goal_state)
    problem.start_state.get_f()
    print("You ran A* search with Misplaced Tile heuristic\n")
    Astar_with_misplaced_tiles(problem)
elif algo == "3":
    #run euclidean here
    print("You ran A* search with Euclidean Distance heuristic\n")
else:
    print("Input not recognized. Please input 1, 2, or 3.")