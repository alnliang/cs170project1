
import copy

def swap( i, j , x, y ,arr):
    arr_copy =copy.deepcopy(arr)
    value_1 = arr_copy[i][j]
    value_2 = arr_copy[x][y]
    arr_copy[i][j]= value_2
    arr_copy[x][y] = value_1
    return arr_copy

class State:
    def __init__(self,first_row = 0,second_row = 0,third_row= 0):
        self.state_rep = [first_row,second_row,third_row]
        self.g = 0
        self.h = 0
        self.f = 0
        #when set first poistion is x-axis, second poistion is y-axis
        self.blank_pos = []
        self.next_states = []
    def set_state_rep(self, state_rep):
        self.state_rep = state_rep
    def set_g(self,g):
        self.g = g
    def set_h(self,h):
        self.h = h
    def get_f(self):
        self.f = self.h +self.g
    def set_blank_pos(self,row_pos,col_pos):
        self.blank_pos = [row_pos,col_pos]
    #used for starting state
    def get_blank_pos(self):
        for i in range(len(self.state_rep)):
            for j in range(len(self.state_rep)):
                if self.state_rep[i][j] == 0:
                    self.blank_pos = [i,j]
    #returns boolean values of wheteher it can move left,right,up,down in that order
    def find_valid_moves(self):
        move_left = True
        move_right = True
        move_up = True
        move_down = True
        #on top
        if self.blank_pos[0] == 0:
            move_up = False
        #on left-hand side
        if self.blank_pos[1] == 0:
            move_left = False
        if self.blank_pos[0] == len(self.state_rep) - 1:
            move_down = False
        if self.blank_pos[1] == len(self.state_rep[0]) - 1:
            move_right = False
        return [move_left, move_right, move_up, move_down]
    def move_up(self):
        next_state_rep = swap(self.blank_pos[0],self.blank_pos[1],self.blank_pos[0]-1, self.blank_pos[1],self.state_rep)
        next_state = State()
        next_state.set_state_rep(next_state_rep)
        next_state.set_g(self.g + 1)
        return next_state
    def move_left(self):
        next_state_rep = swap(self.blank_pos[0],self.blank_pos[1],self.blank_pos[0], self.blank_pos[1]-1,self.state_rep)
        next_state = State()
        next_state.set_state_rep(next_state_rep)
        next_state.set_g(self.g + 1)
        return next_state
    def move_down(self):
        next_state_rep = swap(self.blank_pos[0],self.blank_pos[1],self.blank_pos[0]+1, self.blank_pos[1],self.state_rep)
        next_state = State()
        next_state.set_state_rep(next_state_rep)
        next_state.set_g(self.g + 1)
        return next_state
    def move_right(self):
        next_state_rep = swap(self.blank_pos[0],self.blank_pos[1],self.blank_pos[0], self.blank_pos[1] + 1,self.state_rep)
        next_state = State()
        next_state.set_state_rep(next_state_rep)
        next_state.set_g(self.g + 1)
        return next_state
    def get_next_states(self):
        self.get_blank_pos()
        valid_moves = self.find_valid_moves()
        # for uniform cost search makes sense right and down go before left and up
        # right
        if valid_moves[1] == True:
            right_state = self.move_right()
            self.next_states.append(right_state)
        #down
        if valid_moves[3] == True:
            down_state = self.move_down()
            self.next_states.append(down_state)
        #left
        if valid_moves[0] == True:
            left_state = self.move_left()
            self.next_states.append(left_state)
        #up
        if valid_moves[2] == True:
            up_state = self.move_up()
            self.next_states.append(up_state)
    def print_state_rep(self):
        for row in self.state_rep:
            print(row)

#testing
s = State([1,2,3],[4,0,6],[7,5,8])
# s2 = State()
# print(s.state_rep)
# print(s2.state_rep)
# print(len(s.state_rep))
# s.set_g(1)
# s.set_h(2)
# s.get_f()
s.get_blank_pos()
print(s.blank_pos)
# print(s.g,s.h,s.f, s.blank_pos)
# print(s.find_valid_moves())
s.get_next_states()
print(s.state_rep)
print(s.blank_pos)
print(s.g)
for state in s.next_states:
    print(state.state_rep)
    print(state.g)
l1 = [1,2,3]
curr_item = l1.pop(0)
print(curr_item)
arr1 = [[1,2,3],[4,5,6],[7,8,0]]
arr2 = [[1,2,3],[4,5,6],[7,8,9]]
print(arr1 == arr2)
s.print_state_rep()