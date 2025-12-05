
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
