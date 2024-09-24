import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Sampling frequency, time vector, and frequency of the digital signal
fs, t, frequency = 1000, np.arange(0, 1, 1/1000), 5
# Create the digital signal (1 and -1)
digital_signal = np.sign(np.sin(2 * np.pi * frequency * t))
# Design a low-pass Butterworth filter
# 5th order filter with a cutoff frequency of 10 Hz
b, a = butter(5, 10 / (0.5 * fs), btype='low')
# Apply the low-pass filter to the digital signal to get the analog approximation
analog_signal = lfilter(b, a, digital_signal)


# Plotting
plt.figure(figsize=(12, 6))

# Digital Signal
plt.subplot(2, 1, 1)
plt.title('Baseband Transmission')
plt.plot(t, digital_signal, label='Digital Signal', color='blue')
plt.ylim(-1.5, 1.5)
plt.grid()
plt.ylabel('Amplitude')
plt.legend()

# Analog Approximation
plt.subplot(2, 1, 2)
plt.plot(t, analog_signal, label='Analog', color='orange')
plt.ylim(-1.5, 1.5)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
