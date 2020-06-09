from abc import ABC, abstractmethod
from math import *
from numpy import *

class Point(object):
    count = 0

    @classmethod
    def incrementCount(cls):
        cls.count += 1
        return True

    @classmethod
    def getCount(cls):
        return cls.count

    def __init__(self, x = 0, y = 0, z = 0):
        self.setCoordinates(x, y, z)
        Point.incrementCount()

    def getCoordinates(self):
        return (self.x, self.y, self.z)

    def setCoordinates(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
        return True

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)

    def origin(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    @staticmethod
    def distance(self, other = None):
        if other == None:
            other = Point()
        x = (self.x - other.x) ** 2
        y = (self.y - other.y) ** 2
        z = (self.z - other.z) ** 2
        return (x + y + z) ** 0.5

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    @staticmethod
    def uniformDivision(self, divisor = int()):
        return Point(self.x / divisor, self.y / divisor, self.z / divisor)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

class Segment(object):
    count = 0

    @classmethod
    def getCount(cls):
        return cls.count

    @classmethod
    def incrementCount(cls):
        cls.count += 1
        return True

    def __init__(self, point1 = Point(), point2 = Point()):
        self.setPoints(point1, point2)
        Segment.incrementCount()

    def setPoints(self, point1 = Point(), point2 = Point()):
        self.point1 = point1
        self.point2 = point2
        return True

    def getEndPoints(self):
        return (self.point1, self.point2)

    def midPoint(self):
        return Point.uniformDivision((self.point1 + self.point2), 2)

    def slopeXY(self):
        diff = self.point1 - self.point2
        try:
            return (diff.y / diff.x)
        except:
            return None

    def slopeAngleXY(self):
        return atan(self.slopeXY())

    def __str__(self):
        return self() + " " + self.__name__ + " with slope %f" % (self.slopeXY())

    def __call__(self):
        return "Segment"

    def perpendicularSlopeXY(self):
        return (-1) / self.slopeXY()

    def slopePointForm(self):
        a = self.slopeXY()
        return (a, -1, (a * self.point1.x - self.point1.y))

    def perpBisector(self):
        a = self.perpendicularSlopeXY()
        b = self.midPoint()
        return (a, -1, (a * b.x - b.y))

class Shape(ABC):
    def __init__(self, graphicalPoint = Point()):
        self.setGraphicalPoint(graphicalPoint)

    def setGraphicalPoint(self, graphicalPoint = Point()):
        self.graphicalPoint = graphicalPoint
        return True

    def getGraphicalPoint(self):
        return self.graphicalPoint

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Polygon(Shape):
    count = 0

    @classmethod
    def getCount(cls):
        return cls.count

    @classmethod
    def incrementCount(cls):
        cls.count += 1
        return True
    
    def __init__(self, sides = (), angles = (), graphicalPoint = Point()):
        self.setSides(sides)
        self.setAngles(angles)
        super().__init__(graphicalPoint)
        self.numberOfSides = len(sides)
        Polygon.incrementCount()

    def setSides(self, sides = ()):
        self.sides = sides
        return True

    def setAngles(self, angles = ()):
        self.angles = angles
        return True

    def getSides(self):
        return self.sides

    def getAngles(self):
        return self.angles

    def getNumberOfSides(self):
        self.numberOfSides = len(self.sides)
        return self.numberOfSides

    def __call__(self):
        return "Polygon"

    def __str__(self):
        return self.getNumberOfSides() + " - sided" + self() + " with sides %f and angles %f." % (self.sides, self.angles)

    def isQuadrilateral(self):
        return self.getNumberOfSides() == 4

    def getRegularAngle(self):
        return 180 - (360 / self.getNumberOfSides())

    def getAngleSum(self):
        return self.getNumberOfSides() * self.getRegularAngle()

    def isRegular(self):
        return len(set(sides)) == 1

    def getNumberOfDiagonals(self):
        n = self.getNumberOfSides()
        return n * (n - 3) / 2

    def perimeter(self):
        t = 0
        for i in self.sides:
            t += i
        return t

    @abstractmethod
    def area(self):
        pass

class Quadrilateral(Polygon):
    count = 0

    def __init__(self, sides = (), angles = (), graphicalPoint = Point()):
        super().__init__(sides[:4], angles[:4], graphicalPoint)
        self.setSides(sides[:4])
        self.setAngles(angles[:4])
        Quadrilateral.incrementCount()

    @abstractmethod
    def area(self):
        pass

    def __call__(self):
        return "Quadrilateral"

    def __str__(self):
        return self() + " with sides %s and angles %s" % (self.sides, self.angles)

    def isTrapezium(self):
        return (self.angles[0] + self.angles[1]) == 180

    def isParallelogram(self):
        return (self.sides[0] == self.sides[2]) and self.isTrapezium()

    def isRectangle(self):
        return (self.angles[0] == 90 and self.angles[1] == 90) and self.isParallelogram()

    def isRhombus(self):
        return (self.sides[0] == self.sides[1]) and self.isParallelogram()

    def isSquare(self):
        return self.isRectangle() and self.isRhombus()

class Trapezium(Quadrilateral):
    def __call__(self):
        return "Trapezium"

    def __str__(self):
        return self() + " with sides %s and angles %s." % (self.sides, self.adjAngles)

    def __init__(self, sides = (), adjAngles = (0, 0), graphicalPoint = Point()):
        "Start entering side lengths in clockwise direction from anyone parallel side."
        super().__init__(sides[:4], adjAngles[:2], graphicalPoint)
        self.setAdjacentAngles(adjAngles[:2])

    def getAdjacentAngles(self):
        return self.adjAngles

    def setAdjacentAngles(self, adjAngles = (0, 0)):
        self.adjAngles = adjAngles[:2]
        return True

    def area(self):
        return 0.5 * (self.sides[0] + self.sides[2]) * self.height()

    def height(self, base):
        side = self.side[0]
        angle = self.angles[0]
        if self.sides[0] == base or self.sides[2] == base:
            side = self.adjSides[1]
            angle = self.adjAngles[1]
        return side * sin(angle)

class Parallelogram(Trapezium):
    count = 0

    def __init__(self, adjSides = (0, 0), adjAngles = (0, 0), graphicalPoint = Point()):
        super().__init__(adjSides[:2] * 2, adjAngles[:2] * 2, graphicalPoint)
        self.setAdjacentSides(adjSides[:2])
        Parallelogram.incrementCount()

    def setAdjacentSides(self, adjSides = (0, 0)):
        self.adjSides = adjSides[:2]
        return True

    def getAdjacentSides(self):
        return self.adjSides

    def __str__(self):
        return "Parallelogram"

    def __call__(self):
        return "Parallelogram"

    def area(self):
        a, b = self.adjSides
        return a * self.height(a)

    def perimeter(self):
        a, b = self.adjSides
        return 2 * (a + b)

    def __add__(self, other):
        a, b = self.adjSides
        c, d = other.adjSides
        e, f = self.adjAngles
        g, h = other.adjAngles
        return Parallelogram((a + c, b + d), (e + g, f + h), self.graphicalPoint + other.graphicalPoint)

    @classmethod
    def getCount(cls):
        return cls.count

class Rectangle(Parallelogram):
    count = 0

    def __init__(self, adjSides = (0, 0), adjAngles = (0, 0), graphicalPoint = Point()):
        super().__init__(adjSides[:2], adjAngles[:2], graphicalPoint)
        Rectangle.incrementCount()

    def __str__(self):
        return self() + ": Sides %s and Angles %s" % (self.adjSides, self.adjAngles)

    def __call__(self):
        return "Rectangle"

    def diagonalLength(self):
        return (self.adjSides[0] ** 2 + self.adjSides[0] ** 2) ** 0.5

class Rhombus(Parallelogram):
    count = 0

    def __str__(self):
        return self() + "Side : %f" % (side)

    def __call__(self):
        return "Rhombus"

    def __init__(self, side, adjAngles, graphicalPoint):
        super().__init__((side,) * 2, adjAngles, graphicalPoint)
        Rhombus.incrementCount()

    def getDiagonals(self):
        angle = self.adjAngles[0] / 2
        return (2 * self.adjSides[0] * sin(angle), 2 * self.adjSides[1] * cos(angle))

    def area(self):
        a, b = self.getDiagonals()
        return (a * b / 2)

class Square(Rhombus, Rectangle):
    count = 0

    def __init__(self, side = 0, graphicalPoint = Point()):
        super().__init__((side,) * 2, (90,) * 2, graphicalPoint)
        Square.incrementCount()

    def diagonalLength(self):
        return self.adjSides[0] * (2 ** 0.5)

    def area(self):
        return (self.diagonalLength() ** 2) / 2

    def __str__(self):
        return self() + "Side : %f" % (side)

    def __call__(self):
        return "Square"

class Circle(Shape):
    def __init__(self, center = None, radius = None, referencePoint1 = Point(1, 0 ,0), referencePoint2 = Point(0, 1, 0), referencePoint3 = Point(-1, 0, 0)):
        if(center == None):
            center = self.calCenter(referencePoint1, referencePoint2, referencePoint3)
        self.setCenter(center)
        if(radius == None):
            radius = self.calRadius(referencePoint1)
        self.setRadius(radius)
        super().__init__(self.center)

    def calCenter(self, a, b, c):
        AB = Segment(a, b)
        BC = Segment(b, c)
        CA = Segment(c, a)
        l = [AB.slopeXY(), BC.slopeXY(), CA.slopeXY()]
        if None in l:
            if len(set(l)) == 1:
                return a
            else:
                print("Invalid Points")
                exit() 
        if l.count(0) >= 2:
            print("Invalid Points")
            raise Exception()
            pass
        try:
            index = l.index(0)
        except:
            pass
        if index == 1:
            BC = CA
        if index == 0:
            AB = CA
        A, B, C = AB.perpBisector()
        D, E, F = BC.perpBisector()
        x, y = tuple(linalg.solve(array([[A, B], [D, E]]), array([C, F])))
        return Point(x, y)

    def calRadius(self, point = (0, ) * 3):
        return self.center.distance(point)

    def setCenter(self, center = Point()):
        self.center = center
        return True

    def setRadius(self, radius = 0):
        self.radius  = radius

    def getCenter(self):
        return (self.center.getCoordinates())
    
    def getRadius(self):
        return self.radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def circumference(self):
        return self.perimeter()

    def __call__(self):
        return "Circle"

    def __str__(self):
        return self() + " with center %s and radius %d" % (self.center, self.radius)

    def areConcentric(self, other):
        if(other == None):
            other = Circle()
        return self.center == other.center
