import turtle
 
t = turtle.Turtle()
 
for i in range(5):
    t.forward(150)
    t.right(144)
   
   
   
   def draw_star(size,color):
    count = 0
    angle = 144
    while count <= 5:
        turtle.forward(size)
        turtle.right(angle)
        count += 1
    return
