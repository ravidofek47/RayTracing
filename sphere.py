from typing import Tuple, Union, override

from hitable import HitRecord
from vec3 import Vec3
from ray import Ray
from math import sqrt
# for now its a sphere, later could implement inheritance for more shapes
class Sphere:
    def __init__(self, center: Vec3, r):
        self.center = center
        self.r= r

    @override
    # returns the intersection coordinates of the shape and the ray
    def hit(self, ray : Ray, tmin, tmax) -> Tuple[bool, Union[HitRecord, None]]:

        t1,t2 = self.getIntersectionTs(ray)
        if t1 is None: # no intersections
            return False, None

        tfinal = None

        if tmin < t1 < tmax and tmin < t2 < tmax:
            if abs(t1) < abs(t2): #TODO : make sure this is the intention
                tfinal = t1
            else:
                tfinal = t2

        elif tmin < t1 < tmax: # only t1 is valid
            tfinal = t1
        elif tmin < t2 < tmax:
            tfinal = t2

        if tfinal is None: # no intersections in the tmin tmax
            return False, None

        intPt = ray.at(tfinal)

        hitRecord = HitRecord(intPt, self.getNormal(intPt), 0,tfinal)

        return True, hitRecord

    def getIntersectionTs(self, ray : Ray):
        d = ray.direction
        C = self.center
        Q = ray.origin
        r = self.r

        a = d.dot(d)
        # b = (-2 * d).dot(C - Q)
        c = (C - Q).dot(C - Q) - r * r

        h = d.dot(C - Q)

        disc = h * h - a * c
        if disc < 0:
            return None, None

        root = sqrt(disc)
        t1 = (h + root) / a
        t2 = (h - root) / a
        return t1, t2

    def getNormal(self, intersection):
        return (intersection-self.center).unit()



