#import matplotlib.pyplot as plt

with open("linear_data.csv","r") as f:
    xCoords = []
    yCoords = []
    for line in f.readlines()[1:]:
        x,y = line.split(",")
        xCoords.append(float(x))
        yCoords.append(float(y))
print(xCoords)
print(yCoords)