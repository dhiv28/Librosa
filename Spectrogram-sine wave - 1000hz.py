import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
f = 1000
fs = 25000
dt = 1/fs
t = np.arange(0, 0.01 , dt)
x = np.sin(2 * np.pi * f * t)
plt.plot(t,x)
plt.grid()
plt.show()
spect = lib.stft(x, n_fft = 2048, hop_length= 512)
spect_db = lib.amplitude_to_db(np.abs(spect))
librosa.display.specshow(spect_db, x_axis ='time', y_axis='log')
plt.title('spectrogram')
plt.colorbar()
plt.grid()
plt.show()

"""
Created on Sat Jun  5 12:42:08 2021

@author: Admin
"""

