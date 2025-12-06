import sys
from src.generate import generate

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/generate.py <background|radial_background|image> <params>")
    sys.exit(1)
  
  generateType = sys.argv[1]
  params = sys.argv[2:]
  generate(generateType, 'out', generateType, *params)
