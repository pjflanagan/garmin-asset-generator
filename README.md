
# Garmin Asset Generator

This is a collection of assets drawn for Garmin using code. It will output files fit to all device sizes.

## Include

```py
from src.generate import generate

generate(generateType, outputDir, params)

```

## Run Manually

### Generate Background
```sh
python3 ./main.py background FFFFFF 000000
```

### Resize Image
```sh
python3 ./main.py image ./in/m.png 20
```