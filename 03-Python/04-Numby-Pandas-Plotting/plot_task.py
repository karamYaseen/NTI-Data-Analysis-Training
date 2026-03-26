# Matplotlib in Python - Fourth Day
# This file covers line, scatter, bar, histogram, subplots, styling, grid, and annotations

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]
plt.plot(x, y)
plt.title("Sample Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.scatter(x, y)
plt.title("Sample Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

groups = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]
plt.bar(groups, values)
plt.title("Sample Bar Chart")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 6]
plt.hist(data)
plt.title("Sample Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sample Plot with Subplots")
plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot([1, 2], [10, 20])
ax2.scatter([1, 2], [5, 15])
ax1.set_title("First")
ax2.set_title("Second")
plt.show()

plt.plot([1, 2, 3], [4, 5, 6], color="red", linestyle="--")
plt.title("Styled Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.plot([1, 2, 3], [4, 5, 6])
plt.grid(True)
plt.title("Line Plot with Grid")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.plot([1, 2, 3], [4, 5, 6])
plt.text(2, 5, "Hello")
plt.title("Line Plot with Text Annotation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.plot([1, 2, 3], [4, 5, 6])
plt.annotate("Point", xy=(2, 5), xytext=(2.5, 6), arrowprops=dict(facecolor="black", shrink=0.05))
plt.title("Line Plot with Annotation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
