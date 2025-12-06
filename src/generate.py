import sys
from .asset.background import generate_bowtie_gradient_background, generate_radial_gradient_background
from .asset.image import resize_image_by_percent
from .size import SIZES
from .files import getFolder

GENERATE_TYPE_MAP = {
  "background": generate_bowtie_gradient_background,
  "radial_background": generate_radial_gradient_background,
  "image": resize_image_by_percent,
}

def generate(generateType, directory, name, *args):
  if generateType not in GENERATE_TYPE_MAP:
    raise ValueError(f"Unknown generate type: {generateType}")

  for size in SIZES:
    img = GENERATE_TYPE_MAP[generateType](size, *args)
    folder = getFolder(directory, size, "drawables")
    img.save(folder + f"{name}.png")
