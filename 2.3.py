import numpy as np
import matplotlib.pyplot as plt

# Parameters
frequency = 5      # frequency of the sine wave in Hz
amplitude = 1       # amplitude of the sine wave
sampling_rate = 1000 # sampling rate in Hz
duration = 2        # duration of the signal in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the sine wave
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the signal
plt.figure(figsize=(10, 4))

plt.title('Periodic Signal: Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.plot(t, signal, label=f'{frequency} Hz Sine Wave')
plt.legend()
plt.show()