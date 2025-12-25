from abc import ABC, abstractmethod
from typing import Tuple, Union

from interval import Interval

from ray import Ray
from vec3 import Vec3


class HitRecord(object):
    def __init__(self, point, normal, material, t):
        self.point = point
        self.normal = normal # the normal that points again the ray, the relevant normal
        self.t = t

    def set_face_normal(self, normal):
        self.normal = normal

class Hittable(ABC):
    @abstractmethod
    def hit(self, r: Ray, interval: Interval) -> Tuple[bool, Union[HitRecord, None]]:
        pass


