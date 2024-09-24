import numpy as np
import matplotlib.pyplot as plt

# Set parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector

# Create a composite signal with different frequencies
freq1 = 5    # Frequency of first sine wave
freq2 = 20   # Frequency of second sine wave
composite_signal = np.sin(2 * np.pi * freq1 * t) + 0.8 * np.sin(2 * np.pi * freq2 * t)

# Simulate distortion: Assume different delays for different frequencies
# Set a larger delay for the higher frequency
delay1 = 0.0   # No delay for freq1
delay2 = 0.4   # 0.4 second delay for freq2

# Create received signals with delays
received_signal = np.sin(2 * np.pi * freq1 * (t - delay1)) + 0.8 * np.sin(2 * np.pi * freq2 * (t - delay2))

# Plot the original and received signals
plt.figure(figsize=(15, 8))

# Original Composite Signal
plt.subplot(2, 1, 1)
plt.plot(t, composite_signal, label='Original Composite Signal', color='blue')
plt.title('Original Composite Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.grid(True)
plt.legend()

# Received Signal (with distortion)
plt.subplot(2, 1, 2)
plt.plot(t, received_signal, label='Received Signal (with Distortion)', color='red')
plt.title('Received Signal (with Distortion)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.xlim(0, 1)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
