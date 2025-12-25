import sys
from PIL import Image

from Camera import Camera
from hittable_list import hittable_list
from sphere import Sphere
from vec3 import Vec3

def main():
    # --- argv handling: output file path ---
    if len(sys.argv) < 2:
        print("Usage: python image.py OUTPUT_PPM_PATH", file=sys.stdout)
        sys.exit(1)
    world = hittable_list()
    world.add_hittable(Sphere(Vec3(0.0, -100.5, -1.0), 100.0))
    world.add_hittable(Sphere(Vec3(0.0, 0.0, -1.0), 0.5))
    cam = Camera(out=sys.argv[1])
    cam.render(world)
    img = Image.open(sys.argv[1])
    img.save("final_result.png")  # now open final_result.png in Windows Photos


if __name__ == "__main__":
    main()
