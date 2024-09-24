import numpy as np
import matplotlib.pyplot as plt

# Parameters for the signal
frequency = 4    # Frequency of the sine wave (Hz)
amplitude = 1     # Amplitude of the sine wave
duration = 1      # Duration of the signal (seconds)
sampling_rate = 1000  # Number of samples per second

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration))

# Signal generation
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Plotting the signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title('Analog Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()