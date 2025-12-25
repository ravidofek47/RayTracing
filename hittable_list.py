from typing import override, Tuple, Union

from interval import Interval

from hitable import Hittable, HitRecord
from ray import Ray


class hittable_list(Hittable):
    def __init__(self, objects : list[Hittable] = []):
        self.objects = objects

    def add_hittable(self, hittable : Hittable):
        self.objects.append(hittable)

    @override
    def hit(self, r: Ray, interval:Interval) -> Tuple[bool, Union[HitRecord, None]]:
        hitRecords = []
        for obj in self.objects:

            intersect = obj.hit(r, interval)

            if intersect[0] == True: # intersected with shape
                hitRecords.append(intersect[1])

        if len(hitRecords) == 0:
            return False, None

        minHit = hitRecords[0]
        for hit in hitRecords:
            if abs(hit.t) < abs(minHit.t):
                minHit = hit

        return True, minHit