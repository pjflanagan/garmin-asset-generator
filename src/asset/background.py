import math
from PIL import Image
from color import convert_hex_to_rgb

# generates a bowtie gradient background image at specified pixels
def generate_bowtie_gradient_background(size, backgroundColor, backgroundSecondaryColor):
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

