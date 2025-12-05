import sys
from asset.background import generate_bowtie_gradient_background
from asset.image import resize_image_by_percent
from size import SIZES
from files import getFolder

GENERATE_TYPE_MAP = {
  "background": generate_bowtie_gradient_background,
  "image": resize_image_by_percent,
}

# TODO: come up with a callable function for when this is included in other repos
# def generate(type, size, out):
  

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/generate.py <background|image> <params>")
    sys.exit(1)
  
  generateType = sys.argv[1]
  params = sys.argv[2:]
  for size in SIZES:
    img = GENERATE_TYPE_MAP[generateType](size, *params)
    folder = getFolder(size, "drawables")
    img.save(folder + f"{generateType}.png")
