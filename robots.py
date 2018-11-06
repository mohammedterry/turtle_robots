import turtle as ttl 
import random as rnd

limit = 300
n_walls = 30
too_close = 100

world = ttl.Screen()
world.bgcolor("lightgreen")


robot = ttl.Turtle()
walls = []

for _ in range(n_walls):
    wall = ttl.Turtle()
    wall.speed(10)
    wall.penup()
    wall.shape("circle")
    wall.color("brown")
    x = rnd.random()*limit - limit/2
    y = rnd.random()*limit - limit/2
    # wall.rt(rnd.random()*180)
    # wall.fd(rnd.random()*limit)
    #theta = rnd.random()*360
    #wall.seth(theta)
    wall.goto(x, y)
    walls.append(wall) 

robot.shape("turtle")
robot.color("blue")
# robot.rt(-30)
# robot.fd(100)

for _ in range(500):
    distances = []
    print(robot.pos())
    for wall in walls:
        distance = robot.distance(wall)
        # print(f"distance = {distance}\n coordinates = {wall.pos()}\n\n")
        distances.append((distance,wall.pos()))

    distances = sorted(distances)
    closest_distance = distances[0]
    if closest_distance[0] < too_close:
        closest_coords = closest_distance[1]
        direction_closest = robot.towards(closest_coords)
        robot.seth(direction_closest - 90)
    robot.fd(1)

world.exitonclick()