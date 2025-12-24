import math

from vec3 import Vec3
from interval import Interval
def write_color(out, pixel_color: Vec3):
    interval = Interval(0,1)
    r = math.sqrt(interval.clamp(pixel_color.x()))
    g = math.sqrt(interval.clamp(pixel_color.y()))
    b = math.sqrt(interval.clamp(pixel_color.z()))

    rbyte = int(255.0 * r)
    gbyte = int(255.0 * g)
    bbyte = int(255.0 * b)

    out.write(f"{rbyte} {gbyte} {bbyte}\n")
