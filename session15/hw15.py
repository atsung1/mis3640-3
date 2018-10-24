import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

class Circle:
    """Represents a point in 2-D space.

    attributes: center, radius
    """

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

point_center = Point()
point_center.x = 150
point_center.y = 100
test = Circle()
test.center = point_center
test.radius = 75

def point_in_circle(circle, point):
    c = circle.center
    xdiff = c.x - point.x
    ydiff = c.y - point.y
    return circle.radius >= (math.sqrt(xdiff**2 + ydiff**2))

test_point = Point()
test_point.x = 150
test_point.y = 100
print(point_in_circle(test, test_point))

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    import math
    xdiff = p2.x - p1.x
    ydiff = p2.y - p1.y
    return(math.sqrt(xdiff**2 + ydiff**2))

def rect_in_circle(circle, rect):
    rect_tl = Point()
    rect_tl.x = rect.corner.x
    rect_tl.y = rect.corner.y + rect.height
    rect_tr = Point()
    rect_tr.x = rect.corner.x + rect.width
    rect_tr.y = rect.corner.y + rect.height
    rect_br = Point()
    rect_br.x = rect.corner.x + rect.width
    rect_br.y = rect.corner.y
    
    cnrlst = [rect.corner, rect_tl, rect_tr, rect_br]

    for corner in cnrlst:
        if distance_between_points(corner, circle.center) > circle.radius:
            return False
    return True

test_rectangle = Rectangle()
test_rectangle.width = 10
test_rectangle.height = 20
test_rectangle.corner = test_point
print(rect_in_circle(test, test_rectangle))

# def print_point(p):
#     """Print a Point object in human-readable format."""
#     print('({}, {}).'.format(p.x, p.y))



# def distance_between_points(p1, p2):
#     """Computes the distance between two Point objects.

#     p1: Point
#     p2: Point

#     returns: float
#     """
#     import math
#     xdiff = p2.x - p1.x
#     ydiff = p2.y - p1.y
#     return(math.sqrt(xdiff**2 + ydiff**2))





# def find_center(rect):
#     """Returns a Point at the center of a Rectangle.

#     rect: Rectangle

#     returns: new Point
#     """
#     p = Point()
#     p.x = rect.corner.x + rect.width / 2.0
#     p.y = rect.corner.y + rect.height / 2.0
#     return p


# def print_rectangle(rect):
#     print('width:', rect.width, 'height:', rect.height)
#     print('the lower-left corner:')
#     print_point(rect.corner)