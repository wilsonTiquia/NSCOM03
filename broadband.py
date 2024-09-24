import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector for 1 second
frequency = 5  # Frequency of the digital signal
carrier_frequency = 50  # Frequency of the carrier wave for AM

# Create the digital signal (square wave)
digital_signal = np.sign(np.sin(2 * np.pi * frequency * t))

# Amplitude Modulation
modulated_signal = (1 + digital_signal) * np.sin(2 * np.pi * carrier_frequency * t)

# Plotting
plt.figure(figsize=(12, 6))

# Digital Signal Plot
plt.subplot(2, 1, 1)
plt.title('Digital Signal and AM Modulated Signal')
plt.plot(t, digital_signal, label='Digital Signal', color='blue')
plt.ylim(-1.5, 1.5)
plt.grid()
plt.ylabel('Amplitude')
plt.legend()

# AM Modulated Signal Plot
plt.subplot(2, 1, 2)
plt.plot(t, modulated_signal, label='AM Modulated Signal', color='orange')
plt.ylim(-1.5, 1.5)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
