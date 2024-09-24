import numpy as np
import matplotlib.pyplot as plt

# Parameters
signal_frequency = 5  # Frequency of the signal in Hz
sampling_rate = 100  # Sampling rate in Hz
duration = 1  # Duration in seconds
noise_level = 0.5  # Noise level (standard deviation)

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate a clean signal (sine wave)
signal = np.sin(2 * np.pi * signal_frequency * t)

# Generate noise
noise = np.random.normal(0, noise_level, signal.shape)

# Create a noisy signal
noisy_signal = signal + noise

# Calculate average signal power and average noise power
average_signal_power = np.mean(signal**2)
average_noise_power = np.mean(noise**2)

# Calculate SNR
SNR = average_signal_power / average_noise_power
SNR_db = 10 * np.log10(SNR)

# Print SNR values
print(f"Average Signal Power: {average_signal_power:.4f}")
print(f"Average Noise Power: {average_noise_power:.4f}")
print(f"SNR (linear scale): {SNR:.4f}")
print(f"SNR (dB): {SNR_db:.4f} dB")

# Plot the signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.title("Clean Signal vs Noisy Signal")
plt.plot(t, signal, label='Clean Signal', color='blue')
plt.plot(t, noisy_signal, label='Noisy Signal', color='red', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()
