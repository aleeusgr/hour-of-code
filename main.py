import turtle as t

def draw_petal(heading, lenght, angle):
    t.setheading(heading)
    t.forward(lenght) 
    if lenght < 1:
        return True
    else:  
        return draw_petal(heading + angle, lenght - 10, angle)

# strange flower
def flower(petals, size = 100, tightness = 60):

    ori = tightness*petals
    draw_petal(ori, size, tightness)

    t.pu()
    t.goto((0,0))
    t.pd()

    if petals <= 1:
        return True
    else:
        return flower(petals-1, size, tightness) 

flower(6, 200, 120)

input()
# line()
# f(5)
