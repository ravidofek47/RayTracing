from ray import Ray
from vec3 import Vec3
from object import Object
from ViewPort import Viewport
color = Vec3
class Camera:

    def __init__(self, viewport : Viewport, loc : Vec3, objects ): # objects is : Object[]
        self.viewport = viewport
        self.loc = loc
        self.objects = objects

    def getPixelColor(self, col, row):
        pixelLoc = self.viewport.getPixelLoc(col, row)
        # ray is the sub of loc and slef.loc
        rayDirection = pixelLoc - self.loc
        ray = Ray(self.loc, rayDirection)
        return self.ray_color(ray)

    def ray_color(self, r: Ray):
        intersects = []
        for obj in self.objects:
            intersect1, intersect2 = obj.intersects(r)

            if not intersect1 is None:
                if self.loc.dist(intersect1) < self.loc.dist(intersect2): # closer intersection should count
                    intersects.append([intersect1, obj])
                else:
                    intersects.append([intersect2, obj])

        if len(intersects) == 0:
            return self.getBackgroundColor(r)


        firstIntersect = intersects[0] # simple for now just one intersection assumed
        return firstIntersect[1].getColor(firstIntersect[0]) # shape intersect in the intersection point

        #firstIntersect = min(intersects, TODO: read documentation


    def getBackgroundColor(self, r:Ray):
        direction = r.direction.unit()
        y = direction.y()
        y = (y + 1) / 2
        white = Vec3(1, 1, 1)
        blue = Vec3(0.5, 0.7, 1)
        blendedValue = (1 - y) * white + y * blue
        return blendedValue