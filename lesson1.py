from turtle import*

shape("turtle")
color("orange")
begin_fill()
speed(20)
width(5)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
end_fill()

begin_fill()
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(80, 50)
pendown()

color("blue")
left(90)
forward(15)


penup()
goto(200, 200)
pendown()

begin_fill()
left(120)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20, 150)
pendown()

begin_fill()
width(2)
left(28)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()

penup()
goto(140, 150)
pendown()
 
 
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()




exitonclick()