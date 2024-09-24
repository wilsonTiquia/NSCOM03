import numpy as np
import matplotlib.pyplot as plt

# Parameters for the fundamental frequency
f = 4 # Fundamental frequency in Hz
sampling_rate = 1000  # Number of samples per second
duration = 1  # Duration in seconds

# Time array from 0 to the duration with steps based on the sampling rate
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Sine waves for the composite signal
# Fundamental frequency component
y1 = 1 * np.sin(2 * np.pi * f * t + 0)       # Amplitude 1, no phase shift

# First harmonic (3f) component
y2 = 0.5 * np.sin(2 * np.pi * 3 * f * t + np.pi/4)  # Amplitude 0.5, phase shift π/4

# Second harmonic (9f) component
y3 = 0.25 * np.sin(2 * np.pi * 9 * f * t + np.pi/2)  # Amplitude 0.25, phase shift π/2

# Composite signal: summing the fundamental and harmonic components
composite_signal = y1 + y2 + y3

# Plotting the individual sine waves and composite signal on a single chart
plt.figure(figsize=(10, 6))

# Plot the individual sine waves with different colors
plt.plot(t, y1, label="Fundamental Frequency (f)", color='blue')
plt.plot(t, y2, label="Third Harmonic (3f)", color='orange')
plt.plot(t, y3, label="Ninth Harmonic (9f)", color='green')

# Plot the composite signal in red
#plt.plot(t, composite_signal, label="Composite Signal", color='red', linewidth=2)

# Add labels, title, and legend
plt.title("Composite Signal with Harmonics")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()