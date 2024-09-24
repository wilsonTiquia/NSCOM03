import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
amplitude = 1  # Height of the wave
frequency = 4  # Number of cycles per unit time
duration = 1  # Duration for one full cycle
sampling_rate = 100  # Number of samples per unit time

# Time array from 0 to the duration with a step of 1/sampling_rate
t = np.linspace(0, duration, int(sampling_rate * duration))

# Sine wave formulas with different phase shifts
y_0 = amplitude * np.sin(2 * np.pi * frequency * t + 0)                    # 0 degrees phase shift
y_90 = amplitude * np.sin(2 * np.pi * frequency * t + np.pi / 2)            # 90 degrees phase shift
y_180 = amplitude * np.sin(2 * np.pi * frequency * t + np.pi)               # 180 degrees phase shift
y_270 = amplitude * np.sin(2 * np.pi * frequency * t + 3 * np.pi / 2)       # 270 degrees phase shift

# Plotting all sine waves
plt.figure(figsize=(10, 6))
plt.plot(t, y_0, label="0° Phase Shift")
plt.plot(t, y_90, label="90° Phase Shift")
plt.plot(t, y_180, label="180° Phase Shift")
plt.plot(t, y_270, label="270° Phase Shift")

# Adding labels and title
plt.title("Comparison of Sine Waves with Different Phase Shifts")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
