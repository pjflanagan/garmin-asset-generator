from PIL import Image

def resize_image_by_percent(size, percent_width, image_path):
  """Resize an image based on screen size and percent width."""
  
  image = Image.open(image_path)
  screen_width = size
  new_width = int(screen_width * int(percent_width) / 100)
  
  # Calculate new height maintaining aspect ratio
  aspect_ratio = image.height / image.width
  new_height = int(new_width * aspect_ratio)
  
  return image.resize((new_width, new_height))