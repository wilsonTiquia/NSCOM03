import matplotlib.pyplot as plt
import numpy as np

# Create the data for the columns
#data = [1000, 2000, 3000, 4000, 5000, 6000, 6000, 6000, 5000, 4000, 3000, 2000, 1000]  # Increasing, equal, and decreasing lengths
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,15,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]  # Increasing, equal, and decreasing lengths

# Define the x positions for each column
x = np.arange(len(data))

# Create the column chart
plt.figure(figsize=(10, 5))
plt.bar(x, data, color='skyblue', width=0.4)

# Adding labels and title
plt.title('Bandwidth')

# Set y-ticks to specific values
plt.yticks([])

# Set x-ticks to specific values
plt.xticks([0, len(data) - 1], [1000, 5000])

# Show the plot
plt.grid(False)
plt.show()
