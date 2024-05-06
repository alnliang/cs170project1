from state import State
import heapq
class Problem:
    def __init__(self,start_state):
        self.start_state = start_state
        self.goal_state =[[1,2,3],[4,5,6],[7,8,0]]

import heapq

def uniform_cost_search(Problem):
    frontier = [(Problem.start_state.g, Problem.start_state)]  # Priority queue (heap) to store states based on their cost
    explored = set()  # To keep track of visited states
    count = 0

    while frontier:
        count += 1
        print(count, "node")
        
        _, curr_state = heapq.heappop(frontier)  # Pop state with the lowest cost from the frontier
        print("Current State")
        curr_state.print_state_rep()
        
        if curr_state.state_rep == Problem.goal_state:  # Check if current state is the goal state
            print("Reached Goal")
            break
        print(explored)
        if curr_state.state_rep not in explored:  # Convert list to tuple before checking membership
            explored.add(tuple(curr_state.state_rep))   # Mark the state as visited
            
            curr_state.get_next_states()  # Generate possible next states
            
            for next_state in curr_state.next_states:
                heapq.heappush(frontier, (next_state.g, next_state))  # Push next states into the frontier
    
    print(len(explored), count)

# Example usage:
# uniform_cost_search(YourProblemObject)

        

veryEasy = State([1,2,3], [4,5,6], [7,0,8])
easy = State([1,2,0],[4,5,3],[7,8,6])
doable = State([0, 1, 2], [4, 5, 3], [7, 8, 6])

s = State([1,2,3], [4,8,0], [7,6,5])
p = Problem(s)
uniform_cost_search(p)
arr1 = [[1,1],[2,2]]
arr2 = [[1,1],[2,2]]
arr3 = [[1,1],[1,2]]
print(arr1 == arr2)
print(arr1 == arr3)

