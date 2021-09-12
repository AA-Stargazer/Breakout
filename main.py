from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('blue')
screen.setup(width=1350, height=800)
screen.tracer(0)

x = -800
y = 300
block_dict = {'block-1': Block()}
i = 0

while True:
    if y > -70:
        if x < 700:
            block_dict[f'block{i}'] = Block()
            x += (block_dict[f'block{i}'].size[1]/2 + block_dict[f'block{i-1}'].size[1]/2) * 22
            # I used paper fo this xD but anyway. Looks works fine
            block_dict[f'block{i}'].goto(x, y)
            i += 1
        else:
            x = -800
            y -= 50
    else:
        block_dict[f'block-1'].goto((1000, 1000))
        break

paddle = Paddle()
ball = Ball()
ball.goto(0, -150)

screen.onkeypress(lambda: paddle.go_right(), "Right")  # be careful about that parantheses !!!!!!!!!!!
screen.onkeypress(paddle.go_left, "Left")
screen.listen()

life = 3

scoreboard = Scoreboard(life=life)

while life > 0:
    scoreboard.update_scoreboard()
    scoreboard.life = life
    screen.update()
    ball.move()
    if ball.xcor() > 675:
        ball.goto(ball.xcor() - 10, ball.ycor())
        ball.change_x_direction()
    elif ball.xcor() < -675:
        ball.goto(ball.xcor() + 10, ball.ycor())
        ball.change_x_direction()

    if ball.ycor() > 400:
        ball.goto(ball.xcor(), ball.ycor() - 10)
        ball.change_y_direction()
    elif ball.ycor() < -400:
        ball.goto(ball.xcor(), ball.ycor() + 10)
        ball.reset_position()
        life -= 1

    if ((ball.ycor() - (paddle.ycor() + paddle.shapesize()[0] * 10)) < 1) \
            and paddle.xcor() - paddle.shapesize()[1] * 10 < ball.xcor() < paddle.xcor() + paddle.shapesize()[1] * 10:
        ball.change_y_direction()

    for block in block_dict.values():

        if ball.y_move > 0:
            if (((block.ycor() - block.shapesize()[0] * 10) - ball.ycor()) < 1)\
                    and (block.xcor() - block.shapesize()[1] * 10) < ball.xcor() < (block.xcor() + block.shapesize()[1] * 10)\
                        and (ball.ycor() < block.ycor() - block.shapesize()[0] * 10 + 5):
                block.goto((1000, 1000))
                ball.change_y_direction()
                print(111)
                scoreboard.add_score()
        if ball.y_move < 0:
            if ((ball.ycor() - (block.ycor() + block.shapesize()[0] * 10)) < 1)\
                    and (block.xcor() - block.shapesize()[1] * 10) < ball.xcor() < (block.xcor() + block.shapesize()[1] * 10)\
                        and (ball.ycor() > block.ycor() + block.shapesize()[0] * 10 - 5):
                block.goto((-1000, -1000))
                ball.change_y_direction()
                print(444)
                scoreboard.add_score()

        if ball.x_move > 0:
            if (((block.xcor() - block.shapesize()[1] * 10) - ball.xcor()) < 1) \
                    and (block.ycor() - block.shapesize()[0] * 10) < ball.ycor() < (
                    block.ycor() + block.shapesize()[0] * 10) \
                    and (ball.xcor() < block.xcor() - block.shapesize()[1] * 10 + 5):
                block.goto((1000, 1000))
                ball.change_x_direction()
                print(555)
                scoreboard.add_score()
        elif ball.x_move < 0:
            if ((ball.xcor() - (block.xcor() + block.shapesize()[1] * 10)) < 1) \
                    and (block.ycor() - block.shapesize()[0] * 10) < ball.ycor() < (
                    block.ycor() + block.shapesize()[0] * 10) \
                    and (ball.xcor() > block.xcor() - block.shapesize()[1] * 10 - 5):
                block.goto((1000, 1000))
                ball.change_x_direction()
                print(666)
                scoreboard.add_score()

# TODO make paddle's last movements affect to ball's speed and direction
# TODO make ball thouches in the edge, not in his middle (just add some ball.shapesize values and it's done...)

print(f" your score is: {scoreboard.score}")