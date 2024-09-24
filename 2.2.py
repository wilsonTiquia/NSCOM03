import matplotlib.pyplot as plt
import numpy as np

# Digital signal values
digital_signal = np.array([1, 0, 0, 2, 2,0,0, 0, -1])
# Corresponding y-axis values
y_axis_values = np.array([2, 1, 0, -1, -2])

# Time array (to match the number of values in digital_signal)
t = np.arange(len(digital_signal))

# Plotting the digital signal
plt.figure(figsize=(10, 4))
plt.step(t, digital_signal, where='post', label='Digital Signal')
plt.yticks(y_axis_values)  # Set y-axis ticks to match given values
plt.title('Digital Signal Plot')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()