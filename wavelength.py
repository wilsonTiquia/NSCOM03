import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 3e8  # Speed of light in m/s
f = 1e6  # Reduced frequency for visualization (1 MHz)

# Calculate wavelength
wavelength = c / f  # Wavelength in meters

# Parameters for the sine wave
amplitude = 1  # Height of the wave
cycles = 5  # Number of cycles to plot
duration = cycles * (wavelength / c)  # Duration for multiple cycles
sampling_rate = 100000  # High number of samples for smoothness

# Check if duration is valid
print(f"Duration: {duration} seconds")

# Time array for multiple complete cycles of the sine wave
t = np.linspace(0, duration, int(sampling_rate * duration))

# Check if time array is empty
if t.size == 0:
    print("Time array is empty!")
else:
    print(f"Time array: {t[:5]}...")  # Print first 5 elements

# Sine wave formula: y(t) = A * sin(2πft)
y = amplitude * np.sin(2 * np.pi * f * t)

# Plotting the sine wave
plt.figure(figsize=(12, 6))
plt.plot(t, y, label='Sine Wave', color='blue')
plt.title("Sine Wave Representation (Reduced Frequency)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.axhline(0, color='black', lw=0.5, ls='--')  # Horizontal line at y=0

# Annotate wavelength
for i in range(cycles):
    plt.axvline(x=i * wavelength / c, color='red', linestyle='--', label='Wavelength (λ)' if i == 0 else "")
    plt.text((i + 0.5) * wavelength / c, 0.5, f'λ = {wavelength:.2e} m', color='red', fontsize=10)

# Add grid and legend
plt.grid(True)
plt.legend()
plt.xlim(0, duration)
plt.ylim(-1.2, 1.2)

# Display the plot
plt.show()

# Output the wavelength
print(f"Wavelength of the signal: {wavelength:.2e} m")
