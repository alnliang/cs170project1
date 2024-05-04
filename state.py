class State:
    def __init__(self,first_row,second_row,third_row):
        self.state_rep = [first_row,second_row,third_row]
        self.g = 0
        self.h = 0
        self.f = 0
        self.zero_position = []
        self.NextStates = []
    def set_g(self,g):
        self.g = g
    def set_h(self,h):
        self.h = h
    def set_f(self):
        self.f = self.h +self.g
    

#testing
# s = State([1,2,3],[4,5,6],[7,8,9])
# print(s.state_rep)
# s.set_g(1)
# s.set_h(2)
# s.set_f()
# print(s.g,s.h,s.f)