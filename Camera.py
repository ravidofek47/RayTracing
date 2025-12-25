from ray import Ray
from vec3 import Vec3
from sphere import Sphere
from hitable import Hittable, HitRecord
from ViewPort import Viewport
color = Vec3
class Camera:

    def __init__(self, viewport : Viewport, loc : Vec3): # objects is : Hittable[]
        self.viewport = viewport
        self.loc = loc

    def getPixelColor(self, col, row, world):
        pixelLoc = self.viewport.getPixelLoc(col, row)
        # ray is the sub of loc and slef.loc
        rayDirection = pixelLoc - self.loc
        ray = Ray(self.loc, rayDirection)
        return self.ray_color(ray, world)

    def ray_color(self, r: Ray, world: Hittable):

        firstHit = world.hit(r, 0, 1000) # TODO : determine the range

        if(firstHit[0] == False): # did not hit anyhtinn
            return self.getBackgroundColor(r)
        return self.getColor(firstHit[1]) # shape intersect in the intersection point


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
