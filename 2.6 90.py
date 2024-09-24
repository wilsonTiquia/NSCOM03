import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
amplitude = 1  # Height of the wave
frequency = 4  # Number of cycles per unit time
phase = np.pi / 2  # Phase shift of 90 degrees (π/2 radians)
duration = 1  # Duration for one full cycle
sampling_rate = 100  # Number of samples per unit time

# Time array from 0 to the duration with a step of 1/sampling_rate
t = np.linspace(0, duration, int(sampling_rate * duration))

# Sine wave formula: y(t) = A * sin(2πft + ϕ)
y = amplitude * np.sin(2 * np.pi * frequency * t + phase)

# Plotting the sine wave
plt.plot(t, y)
plt.title("Sine Wave with 90° Phase Shift")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(False)

# Display the plot
plt.show()