import sys
import math
from PIL import Image
from size import SIZES
from files import getFolder


def convert_hex_to_rgb(hex_color):
  """Converts a hex color string (e.g., "#RRGGBB" or "0xRRGGBB") to an RGB tuple."""
  if (hex_color.startswith('0x')):
    hex_color = hex_color[2:]
  elif (hex_color.startswith('#')):
    hex_color = hex_color[1:]
  r = int(hex_color[0:2], 16)
  g = int(hex_color[2:4], 16)
  b = int(hex_color[4:6], 16)

  return (r, g, b)

# generates a bowtie gradient background image at specified pixels
def create_background(backgroundColor, backgroundSecondaryColor, size=1000):
  """Creates a gradient that wraps around the center point twice (bowtie pattern)"""
  img = Image.new('RGB', (size, size))
  pixels = img.load()
  
  center = size / 2
  
  backgroundColor = convert_hex_to_rgb(backgroundColor)
  backgroundSecondaryColor = convert_hex_to_rgb(backgroundSecondaryColor)
  
  for y in range(size):
    for x in range(size):
      # Calculate angle from center
      dx = x - center
      dy = y - center
      angle = math.atan2(dy, dx)
      
      # Normalize angle to 0-1 range and wrap twice (bowtie)
      # atan2 returns -pi to pi, so normalize and multiply by 2 for two cycles
      t = ((angle + math.pi / 4) / (2 * math.pi) * 2) % 1.0
      
      # Create a fade from backgroundColor -> backgroundSecondaryColor -> backgroundColor
      # Use sine wave or triangle wave for smooth transition
      if t < 0.5:
        # First half: fade from backgroundColor to backgroundSecondaryColor
        fade = t * 2
      else:
        # Second half: fade from backgroundSecondaryColor back to backgroundColor
        fade = (1 - t) * 2
      
      # Interpolate between colors
      r = int(backgroundColor[0] * (1 - fade) + backgroundSecondaryColor[0] * fade)
      g = int(backgroundColor[1] * (1 - fade) + backgroundSecondaryColor[1] * fade)
      b = int(backgroundColor[2] * (1 - fade) + backgroundSecondaryColor[2] * fade)
      
      pixels[x, y] = (r, g, b)

  
  return img

# create_background("#550000", "#AA0000").save("background.png")
# create_background("#555555", "#ffffff").save("background.png")


if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/background.py <backgroundColor> <backgroundSecondaryColor>")
    sys.exit(1)
  
  backgroundColor = sys.argv[1]
  backgroundSecondaryColor = sys.argv[2]
  
  for size in SIZES:
    img = create_background(backgroundColor, backgroundSecondaryColor, size)
    folder = getFolder(size, "drawables")
    img.save(folder + "background.png")