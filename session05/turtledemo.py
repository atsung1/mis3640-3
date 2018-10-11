import turtle
from math import pi

jack = turtle.Turtle()

# for i in range(360):

jack.fd(100)
jack.lt(100)

turtle.mainloop()


# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)



# # polygon(jack, 5, 10)


# def circle(t, r):
#     polygon(t, (2*pi*r)/360, 360)


# # jack = turtle.Turtle()

# # circle(jack, 100)

# import turtle
# import math

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
    
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# jack = turtle.Turtle()
# arc(jack, 20, 90)
# turtle.mainloop()
