from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#turn off animation
screen.tracer(0)

#create left and right paddle
r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.right_go_up, "Up")
screen.onkey(r_paddle.right_go_down, "Down")
screen.onkey(l_paddle.left_go_up, "w")
screen.onkey(l_paddle.left_go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #show everything
    ball.move()

    screen.update()

    #detct collission with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.xcor() > 380:
        ball.reset_postion()

        scoreboard.r_point()

    if ball.xcor() < -380:
       ball.reset_postion()

       scoreboard.l_point()



    #detech collission with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -330:
        ball.bounce_x()






screen.exitonclick()
