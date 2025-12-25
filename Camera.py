from ray import Ray
from vec3 import Vec3
from sphere import Sphere
from hitable import Hittable, HitRecord
from ViewPort import Viewport
color = Vec3
class Camera:

    def __init__(self, viewport : Viewport, loc : Vec3, objects : list[Hittable] ): # objects is : Hittable[]
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
        hitRecords = []
        for obj in self.objects:
            intersect = obj.hit(r, -1000, 1000) # TODO : find tmin and tmax

            if intersect[0] == True:
                hitRecords.append(intersect[1]) # TODO : remove obj here and computs the color from camera

        if len(hitRecords) == 0:
            return self.getBackgroundColor(r)


        firstHit= hitRecords[0] # simple for now just one shape intersection assumed
        return self.getColor(firstHit) # shape intersect in the intersection point

        #firstIntersect = min(hitRecords, TODO: read documentation


    def getBackgroundColor(self, r:Ray):
        direction = r.direction.unit()
        y = direction.y()
        y = (y + 1) / 2
        white = Vec3(1, 1, 1)
        blue = Vec3(0.5, 0.7, 1)
        blendedValue = (1 - y) * white + y * blue
        return blendedValue

    def getColor(self, hitRecord : HitRecord):
        # for now, simple, just return the shapes color
        unitNormal = hitRecord.normal
        colorNormal = Vec3((unitNormal.X + 1) / 2, (unitNormal.Y + 1) / 2, (unitNormal.Z + 1) / 2)
        return colorNormal
