import sys
from .asset.background import generate_bowtie_gradient_background
from .asset.image import resize_image_by_percent
from .size import SIZES
from .files import getFolder

GENERATE_TYPE_MAP = {
  "background": generate_bowtie_gradient_background,
  "image": resize_image_by_percent,
}

def generate(generateType, directory, *args):
  if generateType not in GENERATE_TYPE_MAP:
    raise ValueError(f"Unknown generate type: {generateType}")

  for size in SIZES:
    img = GENERATE_TYPE_MAP[generateType](size, *args)
    folder = getFolder(directory, size, "drawables")
    img.save(folder + f"{generateType}.png")

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/generate.py <background|image> <params>")
    sys.exit(1)
  
  generateType = sys.argv[1]
  params = sys.argv[2:]
  generate(generateType, 'out', *params)
