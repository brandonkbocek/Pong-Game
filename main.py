import time
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
from ball import Ball
from paddle import Paddle


def createCenterLine():
    y_pos = -270
    for i in range(0,12):
        segment = Turtle("square")
        segment.color("white")
        segment.shapesize(1, 0.1)
        segment.speed("fastest")
        segment.penup()
        segment.goto(0, y_pos)
        y_pos += 50


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
createCenterLine()
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with right paddle
    if ball.xcor() > 320:
        if ball.distance(right_paddle) < 50:
            ball.bounce_x()

    # detect collision with right paddle
    if  ball.xcor() < -320:
        if ball.distance(left_paddle) < 50:
            ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()


    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()