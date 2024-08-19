import turtle
import random

def setup_screen():
    screen = turtle.Screen()
    screen.title("Horse Racing")
    screen.bgcolor("forestgreen")
    screen.setup(width=1000, height=600)
    return screen

def draw_finish_line():
    finish_line = 400
    turtle.penup()
    turtle.goto(finish_line, 250)
    turtle.right(90)
    turtle.pendown()
    turtle.color("white")
    turtle.width(5)
    turtle.forward(500)
    turtle.hideturtle()

def draw_track():
    track_width = 100
    start_x = -500
    end_x = 400
    starting_positions = [-100, -100, 0, 100]
    turtle.penup()
    for y in starting_positions:
        turtle.goto(start_x, y)
        turtle.pendown()
        turtle.color("white")
        turtle.forward(end_x - start_x)
        turtle.penup()

def create_horses():
    colors = ["red", "blue", "yellow", "orange"]
    names = ["Thunder", "Lightning", "Storm", "Blaze"]
    starting_positions = [-200, -100, 0, 100]
    horses = []
    for i in range(4):
        horse = turtle.Turtle()
        horse.shape("turtle")
        horse.color(colors[i])
        horse.penup()
        horse.goto(-500, starting_positions[i])
        horse.name = names[i]
        horses.append(horse)
    return horses

def move_horse(horse):
    distance = random.randint(1, 10)
    horse.forward(distance)

def race(horses):
    race_on = True
    while race_on:
        for horse in horses:
            move_horse(horse)
            if horse.xcor() > 400:
                race_on = False
                winning_color = horse.color()[0]
                winning_name = horse.name
                turtle.penup()
                turtle.goto(0, 0)
                turtle.color("white")
                turtle.write(f"The winner is {winning_name} ({winning_color})!", align="center", font=("Arial", 24, "bold"))
                turtle.hideturtle()
                return  # Exit the race function after displaying the result

def main():
    screen = setup_screen()
    draw_finish_line()
    draw_track()
    horses = create_horses()
    race(horses)
    turtle.done()  # Properly finish the turtle graphics

if __name__ == "__main__":
    main()
