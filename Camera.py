import sys
import random
from interval import Interval

from ray import Ray
from vec3 import Vec3
from sphere import Sphere
from hitable import Hittable, HitRecord
from ViewPort import Viewport
color = Vec3
class Camera:

    def __init__(self, out, loc : Vec3 = Vec3(0,0,0)): # objects is : Hittable[]
        self.viewport = Viewport(aspect_ratio=1.7778, image_width=400, viewport_height=2, depth=-1)
        self.loc = loc
        self.out_path = out
        self.samples_per_pixel = 5

    def render(self, world: Hittable):
        image_width = self.viewport.getImageWidth()
        image_height = self.viewport.getImageHeight()

        # Open the output file instead of writing to stdout
        with open(self.out_path, "w") as out:
            # PPM header
            out.write(f"P3\n{image_width} {image_height}\n255\n")
            # Render
            for row in range(image_height):
                # Log with print (to stderr)
                print(
                    f"\rScanlines remaining: {image_height - row} ",
                    end="",
                    file=sys.stdout,
                    flush=True,
                )
                for col in range(image_width):
                    pixel_color = self.getPixelColor(col, row, world)
                    self.write_color(out, pixel_color)
        print("\rDone.                 ", file=sys.stdout)

    def ray_color(self, r: Ray, world: Hittable):

        firstHit = world.hit(r, Interval(0, 1000)) # TODO : determine the range

        if(firstHit[0] == False): # did not hit anyhtinn
            return self.getBackgroundColor(r)
        return self.getColor(firstHit[1]) # shape intersect in the intersection point

    def getPixelColor(self, col, row, world):
        avgColor = Vec3(0,0,0)
        for i in range(self.samples_per_pixel):
            ray = self.get_ray(col, row)
            avgColor += self.ray_color(ray, world)

        avgColor = avgColor / self.samples_per_pixel

        return avgColor

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

    def write_color(self, out, pixel_color):
        """Write one pixel to the given output stream in PPM format."""
        interval: Interval = Interval(0, 1)
        r = interval.clamp(pixel_color.x())
        g = interval.clamp(pixel_color.y())
        b = interval.clamp(pixel_color.z())


        # Translate [0,1] to [0,255]
        rbyte = int(255 * r)
        gbyte = int(255 * g)
        bbyte = int(255 * b)

        out.write(f"{rbyte} {gbyte} {bbyte}\n")

    def get_ray(self, col, row):
        pixelLoc = self.viewport.getPixelLoc(col, row)
        # ray is the sub of loc and slef.loc
        rayDirection = pixelLoc - self.loc
        return Ray(self.loc, rayDirection)


