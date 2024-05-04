from state import State
from problem import Problem

def read_user_input(s):
    result = s.split(',')
    result = [int(x) for x in result]
    return result


print("Welcome to XXX (change this to your student ID) 8 puzzle solver.")
option  = input( "Type “1” to use a default puzzle, or “2” to enter your own puzzle.")
print(option)
# if option == 1
# have a predetermined state asshown 
#if option  == 2 
print("Enter your puzzle, use a zero to represent the blank")
first_row = input( "Enter the first row, use commas between numbers")
second_row = input( "Enter the second row, use commas between numbers")
third_row = input( "Enter the third row, use commas between numbers")
first_row = read_user_input(first_row)
second_row = read_user_input(second_row)
third_row = read_user_input(third_row)
start_state = State(first_row, second_row, third_row)
print(start_state.state_rep)
