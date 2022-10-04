import numpy as np
import matplotlib.pyplot as plt

x = []
y = []

file = "testdata.txt"

with open(file, "r") as fil:
    for i in fil:
        i = i.split(";")
        #print(i)
        x.append(i[1][5:].replace("-", "."))
        y.append(float(i[2].rstrip("\n")))

print(x, y)
plt.plot(x, y, "bo")

plt.show()