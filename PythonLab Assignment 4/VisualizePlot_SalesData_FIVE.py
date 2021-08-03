import matplotlib.pyplot as plt

years = [1991, 1992, 1993, 1994, 1995]
total_populations = [8939127, 8954658, 8960457, 8956841, 8943761]

plt.plot(years, total_populations)
plt.title("Year vs Population in Bulgaria")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()
