from typing import override, Tuple, Union

from hitable import Hittable, HitRecord
from ray import Ray


class hittable_list(Hittable):
    def __init__(self, objects : list[Hittable]):
        self.objects = objects

    @override
    def hit(self, r: Ray, t_min, t_max) -> Tuple[bool, Union[HitRecord, None]]:
        hitRecords = []
        for obj in self.objects:

            intersect = obj.hit(r, t_min, t_max)

            if intersect[0] == True: # intersected with shape
                hitRecords.append(intersect[1])

        if len(hitRecords) == 0:
            return False, None

        minHit = hitRecords[0]
        for hit in hitRecords:
            if abs(hit.t) < abs(minHit.t):
                minHit = hit

        return True, minHit