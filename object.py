from vec3 import Vec3
from ray import Ray
from math import sqrt
# for now its a sphere, later could implement inheritance for more shapes
class Object:
    def __init__(self, center: Vec3, r, color : Vec3):
        self.center = center
        self.r= r
        self.color = color


    # returns the intersection coordinates of the shape and the ray
    def intersects(self, ray : Ray):

        d = ray.direction
        C = self.center
        Q = ray.origin
        r = self.r

        a = d.dot(d)
        b = (-2 * d).dot(C - Q)
        c = (C - Q).dot(C - Q) - r * r


        disc = b*b - 4*a*c
        if disc <0:
            return None, None

        root = sqrt(disc)
        t1 = (-b + root)/(2*a)
        t2 = (-b - root)/(2*a)

        return ray.at(t1), ray.at(t2)

    def getColor(self, intersection):
        #for now, simple, just return the shapes color
        unitNormal = (intersection-self.center).unit()
        colorNormal = Vec3((unitNormal.X+1)/2, (unitNormal.Y+1)/2, (unitNormal.Z+1)/2)
        return colorNormal


