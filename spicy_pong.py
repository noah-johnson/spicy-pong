import turtle
import math
import random

###### Draw window ######

window = turtle.Screen()
window.bgcolor("Black")
window.title("Spicy Pong")

###### Create Paddles ######

paddle_1 = turtle.Turtle()
paddle_1.color("white")
paddle_1.shape("square")
paddle_1.turtlesize(0.5, 1.7)
paddle_1.penup()
paddle_1.speed(4) # Draw slower for cool slide-in effect
paddle_1.setposition(-380, 0)
paddle_1.setheading(90)

paddle_2 = turtle.Turtle()
paddle_2.color("white")
paddle_2.shape("square")
paddle_2.turtlesize(0.5, 1.7)
paddle_2.penup()
paddle_2.speed(4) # Draw slower for cool slide-in effect
paddle_2.setposition(380, 0)
paddle_2.setheading(90)


###### Paddle Movement ######
paddle_speed = 20

def move_paddle_1_up():
  y = paddle_1.ycor()
  y += paddle_speed
  if y > 360:
    y = 360
  paddle_1.sety(y)

def move_paddle_1_down():
  y = paddle_1.ycor()
  y -= paddle_speed
  if y < -350:
    y = -350
  paddle_1.sety(y)

def move_paddle_2_up():
  y = paddle_2.ycor()
  y += paddle_speed
  if y > 360:
    y = 360
  paddle_2.sety(y)

def move_paddle_2_down():
  y = paddle_2.ycor()
  y -= paddle_speed
  if y < -350:
    y = -350
  paddle_2.sety(y)

###### Create Ball ######
ball = turtle.Turtle()
ball.setposition(0, 0)
ball.color("white")
ball.shape("circle")
ball.turtlesize(0.6)
ball.penup()
ball.speed(0)

ball_speed = 7

###### Key Bindings ######
turtle.listen()
turtle.onkey(move_paddle_1_up, "q")
turtle.onkey(move_paddle_1_down, "a")
turtle.onkey(move_paddle_2_up, "o")
turtle.onkey(move_paddle_2_down, "l")

###### Game Functions ######
def isCollision(turtle1, turtle2):
  distance = math.hypot((turtle2.xcor() - turtle1.xcor()),(turtle2.ycor() - turtle1.ycor()))
  if distance < 22:
    return True

player_1_score = 0
player_2_score = 0

###### Main Game Loop ######
while True:
  # Reverse the ball direction if it hits a paddle
  if isCollision(ball, paddle_1) or isCollision(ball, paddle_2):
    # Give the ball a little push to prevent "sticky hits"
    if ball_speed > 0:
      ball.setx(ball.xcor() - 10)
    if ball_speed < 0:
      ball.setx(ball.xcor() + 10)
    ball_speed *= -1

  # Reflect ball from top wall
  if ball.ycor() > 375:
    ball.sety(ball.ycor() - 10)

  # Reflect ball from bottom wall
  if ball.ycor() < -370:
    ball.sety(ball.ycor() + 10)

  # Move the ball forward along the x axis
  ball.setx(ball.xcor() + ball_speed)

  # Set a random value to bump the ball up and down by
  ball_spicy_factor = random.randint(-7,7)
  ball.sety(ball.ycor() + ball_spicy_factor)

  # Reset ball if a paddle fails to hit it 
  if ball.xcor() > 380:
    ball_speed *= -1 
    ball.setx(0)
    player_1_score += 1
    print("Player 1 score:")
    print(player_1_score)

  if ball.xcor() < -380:
    ball_speed *= -1 
    ball.setx(0)
    player_2_score += 1
    print("Player 2 score:")
    print(player_2_score)

  if player_1_score >= 10:
    print("Player 1 is the spiciest!")
    break

  if player_2_score >= 10:
    print("Player 2 is the spiciest!")
    break
