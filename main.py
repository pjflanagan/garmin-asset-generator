import sys
from src.generate import generate

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: python3 ./src/generate.py <background|radial_background|image> fileName <params>")
    sys.exit(1)
  
  generateType = sys.argv[1]
  outputName = sys.argv[2]
  params = sys.argv[3:]
  generate(generateType, 'out', outputName, *params)