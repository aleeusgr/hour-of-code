import turtle as t

def draw_petal(heading, length, angle):
    t.setheading(heading)
    t.forward(length) 
    if length < 1:
        return True
    else:  
        return draw_petal(heading + angle, length - 10, angle)

# strange flower
def flower(petals, complexity = 100, tightness = 60):

    ori = tightness*petals # note logic here
    draw_petal(ori, complexity, tightness)

    t.pu()
    t.goto((0,0))
    t.pd()

    if petals <= 1:
        return True
    else:
        return flower(petals-1, complexity, tightness) 

flower(9, 100, 78) # number of petals and the angle are linked?

input()
# line()
# f(5)
