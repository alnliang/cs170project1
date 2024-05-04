class State:
    def __init__(self,first_row,second_row,third_row):
        self.state_rep = [first_row,second_row,third_row]
        self.g = 0
        self.h = 0
        self.f = 0
        #when set first poistion is x-axis, second poistion is y-axis
        self.blank_pos = []
        self.NextStates = []
    def set_g(self,g):
        self.g = g
    def set_h(self,h):
        self.h = h
    def set_f(self):
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
    

#testing
s = State([1,2,3],[4,5,6],[7,8,0])
print(s.state_rep)
print(len(s.state_rep))
s.set_g(1)
s.set_h(2)
s.set_f()
s.get_blank_pos()
print(s.g,s.h,s.f, s.blank_pos)
print(s.find_valid_moves())