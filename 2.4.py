import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 20  # sampling rate in Hz
duration = 2          # duration of the signal in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate a non-periodic signal: Example - Random noise
np.random.seed(0)  # Seed for reproducibility
signal = np.random.normal(0, 1, size=t.shape)  # Gaussian noise with mean 0 and standard deviation 1




# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label='Non-Periodic Signal')
plt.title('Non-Periodic Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()