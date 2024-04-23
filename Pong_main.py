from turtle import Turtle,Screen
from pong_creation import Pong
import time
from score_board import Score
from ball import Ball


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball=Ball()
paddle_a = Pong((-280, 0))
paddle_b = Pong((280, 0))
#scoreboard=Score()

score1 = Score((-100, 250))
score2 = Score((100, 250))
# screen.listen()
# screen.onkeypress(pong.up, "Up")
# screen.onkeypress(pong.down, "Down")
# screen.onkeypress(pong.w, "w")
# screen.onkeypress(pong.s, "s")
screen.listen()
screen.onkeypress(paddle_a.move_up, "w")
screen.onkeypress(paddle_a.move_down, "s")
screen.onkeypress(paddle_b.move_up, "Up")
screen.onkeypress(paddle_b.move_down, "Down")
game_on=True
score_increment = 0

while game_on:
    while game_on:
        screen.update()
        time.sleep(0.009)
        ball.refresh()

        if ball.ycor() > 270 or ball.ycor() < -270:
            ball.bounce()
        if ball.distance(paddle_b) < 50 and ball.xcor() > 260 or ball.distance(paddle_a) < 50 and ball.xcor() < -260:
            ball.x_bounce()

        if ball.xcor() < -380:
            ball.reset_position()
            score2.update_score()
            score_increment += 1
            if score_increment % 5 == 0:
                ball.increase_speed()

        if ball.xcor() > 380:
            ball.reset_position()
            score1.update_score()
            score_increment += 1
            if score_increment % 5 == 0:
                ball.increase_speed()
screen.exitonclick()