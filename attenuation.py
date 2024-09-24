import numpy as np
import matplotlib.pyplot as plt

# Set the parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector

# Create a random original signal
np.random.seed(0)  # For reproducibility
original_signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(fs)

# Simulate attenuation (e.g., -10 dB)
attenuation_db = -10
attenuation_factor = 10 ** (attenuation_db / 20)
attenuated_signal = original_signal * attenuation_factor

# Simulate amplification (e.g., +10 dB)
amplification_db = 10
amplification_factor = 10 ** (amplification_db / 20)
amplified_signal = original_signal * amplification_factor

# Plot the signals
plt.figure(figsize=(15, 8))

# Original Signal
plt.subplot(3, 1, 1)
plt.plot(t, original_signal, label='Original Signal', color='blue')
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Attenuated Signal
plt.subplot(3, 1, 2)
plt.plot(t, attenuated_signal, label='Attenuated Signal', color='red')
plt.title('Attenuated Signal (-10 dB)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Amplified Signal
plt.subplot(3, 1, 3)
plt.plot(t, amplified_signal, label='Amplified Signal (+10 dB)', color='green')
plt.title('Amplified Signal (+10 dB)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
