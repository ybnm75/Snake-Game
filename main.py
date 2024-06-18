import time
from turtle import Screen

from Snake_game.food import Food
from Snake_game.scoreboard import ScoreBoard
from Snake_game.snake import Snake

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()
screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_in_on = True
while game_in_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.setScore()

    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreBoard.gameOver()

    # Detection collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_in_on = False
            scoreBoard.gameOver()


screen.exitonclick()
