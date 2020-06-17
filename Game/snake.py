from turtle import *
from random import *
from base import vector, square


def run_game():
    win = Screen()
    win.title("risla's snake game")
    food = vector(0, 0)
    snake = [vector(50, 50)]
    speed = 10
    aim = vector(0, -speed)
    win.clearscreen()
    pen = Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("pink")
    pen.penup()
    pen.hideturtle()
    pen.goto(10, 170)
    pen.clear()
    pen.write("Score: 0 ", align="center", font=("Courier", 24, "normal"))

    def change(x, y):
        aim.x = x
        aim.y = y

    def inside(head):
        return -200 < head.x < 190 and -200 < head.y < 190


    def move():
        head = snake[-1].copy()
        head.move(aim)
        snake.append(head)
        rest = snake.copy()
        rest.pop()
        if not inside(head) or head in rest:
            for body in snake:
                square(body.x, body.y, 10, "red")
            update()
            win.clearscreen()
            pen.clear()
            pen.goto(0, -50)
            pen.color("red")
            pen.write("Score: {} ".format((len(rest) - 1) * 10), align="center", font=("Courier", 24, "normal"))
            restart = win.textinput("Game over !", "Do you want to restart ? (y/n)")
            if restart == "y":
                win.resetscreen()
                run_game()

            return
        if food == head:
            print("Snake point : ", len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
            pen.clear()
            pen.write("Score: {} ".format((len(snake)-1)*10), align="center", font=("Courier", 24, "normal"))

        else:
            snake.pop(0)
        clear()
        for body in snake:
            square(body.x, body.y, 10, "Green")
        square(food.x, food.y, 10, "black")
        update()
        ontimer(move, 100)


    win.setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(speed, 0), "Right")
    onkey(lambda: change(-speed, 0), "Left")
    onkey(lambda: change(0, speed), "Up")
    onkey(lambda: change(0, -speed), "Down")
    move()
    done()


run_game()
