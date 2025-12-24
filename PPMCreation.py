import sys
from PIL import Image
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

    # Image
    image_width = 256
    image_height = 256

    # Open the output file instead of writing to stdout
    with open(out_path, "w") as out:
        # PPM header
        out.write(f"P3\n{image_width} {image_height}\n255\n")

        # Render
        for j in range(image_height):
            # Log with print (to stderr)
            print(
                f"\rScanlines remaining: {image_height - j} ",
                end="",
                file=sys.stdout,
                flush=True,
            )
            for i in range(image_width):

                r = i / (image_width - 1)
                g = j/ (image_height - 1)
                b = 0.0
                rbyte = int(255 * r)
                gbyte = int(255 * g)
                bbyte = int(255 * b)
                out.write(f"{rbyte} {gbyte} {bbyte}\n")

    print("\rDone.                 ", file=sys.stdout)

if __name__ == "__main__":
    main()
    img = Image.open(sys.argv[1])
    img.save("final_result.png")
