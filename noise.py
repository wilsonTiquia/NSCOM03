import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector
freq = 5  # Frequency of the clean signal

# Generate a clean sine wave signal
clean_signal = np.sin(2 * np.pi * freq * t)

# Add Thermal Noise
thermal_noise = np.random.normal(0, 0.1, fs)  # Mean = 0, Std = 0.1
signal_with_thermal_noise = clean_signal + thermal_noise

# Add Induced Noise
induced_noise = 0.5 * np.sin(2 * np.pi * 50 * t)  # Simulated appliance noise
signal_with_induced_noise = signal_with_thermal_noise + induced_noise

# Add Cross Talk
crosstalk_signal = 0.3 * np.sin(2 * np.pi * 10 * t)  # Another signal
signal_with_crosstalk = signal_with_induced_noise + crosstalk_signal

# Add Impulse Noise
impulse_noise = np.zeros(fs)
impulse_indices = np.random.choice(fs, 5, replace=False)  # 5 random impulses
impulse_noise[impulse_indices] = np.random.normal(0, 5, 5)  # Impulse values
signal_with_impulse_noise = signal_with_crosstalk + impulse_noise

# Plotting with smaller size
plt.figure(figsize=(10, 8))  # Smaller figure size
plt.subplot(5, 1, 1)
plt.title("Clean Signal")
plt.plot(t, clean_signal)

plt.subplot(5, 1, 2)
plt.title("Signal with Thermal Noise")
plt.plot(t, signal_with_thermal_noise)

plt.subplot(5, 1, 3)
plt.title("Signal with Induced Noise")
plt.plot(t, signal_with_induced_noise)

plt.subplot(5, 1, 4)
plt.title("Signal with Cross Talk")
plt.plot(t, signal_with_crosstalk)

plt.subplot(5, 1, 5)
plt.title("Signal with Impulse Noise")
plt.plot(t, signal_with_impulse_noise)

plt.tight_layout()
plt.show()
