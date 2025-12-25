import sys
from PIL import Image

from Camera import Camera
from ViewPort import Viewport
from object import Object
from vec3 import Vec3
color = Vec3
def write_color(out, pixel_color):
    """Write one pixel to the given output stream in PPM format."""
    r = pixel_color.x()
    g = pixel_color.y()
    b = pixel_color.z()

    # Translate [0,1] to [0,255]
    rbyte = int(255 * r)
    gbyte = int(255 * g)
    bbyte = int(255 * b)

    out.write(f"{rbyte} {gbyte} {bbyte}\n")

def main():
    # --- argv handling: output file path ---
    if len(sys.argv) < 2:
        print("Usage: python image.py OUTPUT_PPM_PATH", file=sys.stderr)
        sys.exit(1)
    out_path = sys.argv[1]

    viewPort = Viewport(aspect_ratio=1.7778, image_width=400, viewport_height=2, depth=-1)

    objects =[]
    objects.append(Object(Vec3(0,0, -1), 0.5, color(1,0, 0)))

    camera = Camera(viewPort, Vec3(0,0,0), objects)
    # Image
    image_width = viewPort.getImageWidth()
    image_height = viewPort.getImageHeight()

    # Open the output file instead of writing to stdout
    with open(out_path, "w") as out:
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
                pixel_color = camera.getPixelColor(col, row)
                write_color(out, pixel_color)
    print("\rDone.                 ", file=sys.stdout)
    img = Image.open(sys.argv[1])
    img.save("image.png")  # now open final_result.png in Windows Photos

if __name__ == "__main__":
    main()
