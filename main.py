import turtle as t

# function with a parameter which has default value, 
def f(i = 1):
    print(i)

def draw_line(l = 100):
    t.forward(l)
# recursive line:
def recursive_line(lenght = 100, heading = 0):
    t.forward(lenght) 
    t.setheading(heading)
    if lenght < 1:
        return input()
    else:  
        return recursive_line(lenght - 10, heading + 10)

recursive_line()
# line()
# f(5)
input()
