from state import State
import heapq
class Problem:
    def __init__(self,start_state):
        self.start_state = start_state
        self.goal_state =[[1,2,3],[4,5,6],[7,8,0]]

def general_problem(Problem):
    frontier = [Problem.start_state]
    explored = []
    can_explore = True
    count = 0
    while can_explore:
        count += 1
        print(count , "node")
        # print(len(frontier))
        # for state in frontier:
        #     state.print_state_rep()
        #     print("-------")
        if len(frontier) == 0:
            print("Fails")
            break
        curr_state = frontier.pop(0)
        print("Current State")
        curr_state.print_state_rep()
        explored.append(curr_state.state_rep)
        if curr_state.state_rep == Problem.goal_state:
            print("Reached Goal")
            can_explore = False
            break
        curr_state.get_next_states()
        same = True
    
        for next_state in curr_state.next_states:
            if next_state.state_rep not in explored:
                print("added to frontier")
                next_state.print_state_rep()
                frontier.append(next_state)
    print(len(explored), count)
        

veryEasy = State([1,2,3], [4,5,6], [7,0,8])
easy = State([1,2,0],[4,5,3],[7,8,6])
doable = State([0, 1, 2], [4, 5, 3], [7, 8, 6])

s = State([1,2,3], [4,8,0], [7,6,5])
p = Problem(s)
general_problem(p)
arr1 = [[1,1],[2,2]]
arr2 = [[1,1],[2,2]]
arr3 = [[1,1],[1,2]]
print(arr1 == arr2)
print(arr1 == arr3)

