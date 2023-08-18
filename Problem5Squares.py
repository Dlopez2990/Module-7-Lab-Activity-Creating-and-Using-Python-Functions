import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

# Call the drawSquare function to draw a blue square with size 100
drawSquare(alex, 100)

# Move the turtle to the starting position for the inner square
alex.penup()
alex.forward(25)  
alex.left(90)
alex.forward(25)  # inner square
alex.right(90)
alex.pendown()

# Draw a small square
alex.color("blue")
drawSquare(alex, 50)  # inner square here

# Move the turtle to the starting position for the second inner square
alex.penup()
alex.forward(12.5)  
alex.left(90)
alex.forward(12.5)  # second inner square
alex.right(90)
alex.pendown()

# Draw an even smaller square
alex.color("blue")
drawSquare(alex, 25)  # second inner square here

# Move the turtle to the starting position for the third inner square
alex.penup()
alex.forward(6.25)  
alex.left(90)
alex.forward(6.25)  # third inner square
alex.right(90)
alex.pendown()

#  Draw an even smaller purple square inside the blue square
alex.color("blue")
drawSquare(alex, 12.5)  # third inner square here

# Move the turtle to the starting position for the fourth inner square
alex.penup()
alex.backward(6.25) 
alex.right(90)
alex.forward(6.25)  # fourth inner square
alex.left(90)
alex.pendown()

# Draw the same shape between the second inner
drawSquare(alex, 25)  

wn.exitonclick()
