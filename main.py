import turtle as t

def draw_petal(heading, legnth, angle):
    t.setheading(heading)
    t.forward(legnth) 
    if legnth < 1:
        return True
    else:  
        return draw_petal(heading + angle, legnth - 10, angle)

# strange flower
def flower(petals, complexity = 100, tightness = 60):

    ori = tightness*petals
    draw_petal(ori, complexity, tightness)

    t.pu()
    t.goto((0,0))
    t.pd()

    if petals <= 1:
        return True
    else:
        return flower(petals-1, complexity, tightness) 

flower(6, 200, 60)

input()
# line()
# f(5)
