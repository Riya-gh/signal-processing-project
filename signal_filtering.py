import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Generate a Time Axis
fs = 500  # Sampling frequency (Hz)
T = 2.0 / fs  # Sampling period
t = np.arange(0, 1, T)  # 1 second of time

# Generate a Composite Signal (Two sine waves)
f1 = 50  # Frequency of first signal (Hz)
f2 = 50  # Frequency of second signal (Hz)
signal = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Plot the Original Signal
plt.figure(figsize=(10, 4))
plt.plot(t, signal, label="Signal")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Original Signal in Time Domain")
plt.legend()
plt.grid()

# Perform Fourier Transform
fft_signal = fft(signal)
frequencies = np.fft.fftfreq(len(t), T)

# Plot Frequency Spectrum
plt.figure(figsize=(10, 4))
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_signal[:len(frequencies)//2]), label="Magnitude Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Domain (FFT)")
plt.legend()
plt.grid()

plt.show()
