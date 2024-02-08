from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
s = -100
turtle_list = []
for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=s)
    s += 50

is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        move = random.randint(0, 10)
        turtle.forward(move)
        if turtle.xcor() > 220:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You've won! Winner turtle is {winner_color}")
            else:
                print(f"Sorry you lost. Winner turtle is {winner_color}")

screen.exitonclick()
