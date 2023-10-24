import turtle as t

def recursive_line(heading, lenght):
    if heading >= 360:
        heading -=360
    t.forward(lenght) 
    t.setheading(heading)
    if lenght < 1:
        return True
    else:  
        return recursive_line(heading + 80, lenght - 10)

# strange flower
for i in range(6):
    recursive_line(i*60,100)
    t.pu()
    t.goto((0,0))
    t.pd()

input()
# line()
# f(5)
