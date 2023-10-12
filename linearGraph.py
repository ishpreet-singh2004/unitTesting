import matplotlib.pyplot as plt
import pandas
import numpy as np
with open("linear_data.csv","r") as f:
    xCoords = []
    yCoords = []
    for line in f.readlines()[1:]:
        x,y = line.split(",")
        xCoords.append(float(x))
        yCoords.append(float(y))
plt.scatter(xCoords,yCoords)
plt.show()
def linear_regression(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    sigmax  = np.std(x)
    sigmay  = np.std(y)
    sigmaxy = np.sum(np.multiply(x-meanx,y-meany))/(len(x)-1)
    m = sigmaxy/(sigmax*sigmax)
    q = meany-m*meanx
    return m,q

x = xCoords
y = yCoords
lin_reg_m_tot, lin_reg_g_tot = linear_regression(x,y)
print(lin_reg_m_tot)
print(lin_reg_g_tot)

lin_reg_m_tot, lin_reg_q_tot = linear_regression(xCoords,yCoords)
y_tot = xCoords*lin_reg_m_tot+lin_reg_q_tot
plt.plot(xCoords, y_tot, label="Lin.",color ='r')
plt.legend()

plt.scatter(xCoords,yCoords)


plt.xlabel("x Coordinates")
plt.ylabel("y Coordinates")
plt.title("Scatter Plot")

plt.show()

def correlation_coefficient(xCoords,yCoords):
    meanx   = np.mean(xCoords)
    meany   = np.mean(yCoords)
    sigmax  = np.std(xCoords)
    sigmay  = np.std(yCoords)
    sigmaxy = np.sum(np.multiply(x-meanx,y-meany))/(len(x)-1)
    correlation = sigmaxy/(sigmax*sigmay)
    return correlation
c_correlation= correlation_coefficient((xCoords,yCoords))
print(c_correlation)
