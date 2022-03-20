from turtle import Screen
from score_board import Score
from food import Food
import time
from snake import Snake

move_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while move_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.increase()

    # Detect collision with wall

    if snake.head.ycor() <= -300 or snake.head.ycor() >= 320:
        scoreboard.lose()
        break

    if snake.head.xcor() <= -300 or snake.head.xcor() >= 300:
        scoreboard.lose()
        break

    # Detect collision with own tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            move_on = False
            scoreboard.lose()

with open('data.txt', 'r') as file:
    greatest_score = file.readline()
    if int(scoreboard.score) > int(greatest_score):
        with open('data.txt', 'w') as new_score:
            new_score.write(f'{scoreboard.score}')

screen.exitonclick()
