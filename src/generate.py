import sys
from asset.background import generate_bowtie_gradient_background
from size import SIZES
from files import getFolder

GENERATE_TYPE_MAP = {
  "background": generate_bowtie_gradient_background,
  # "second-hand": 
}

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/generate.py <type> <params>")
    sys.exit(1)
  
  generateType = sys.argv[1]
  params = sys.argv[2:]
  for size in SIZES:
    img = GENERATE_TYPE_MAP[generateType](size, *params)
    folder = getFolder(size, "drawables")
    img.save(folder + f"{generateType}.png")
