

r = 0
g = 0
b = 0
i = 0

for r in range(0,4,1):
    for g in range(0,4,1):
        for b in range(0,4,1):
            color = f'{r*85:02X}{g*85:02X}{b*85:02X}'
            i += 1
            print(color)

print (f'Total colors: {i}')
