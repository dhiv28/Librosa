import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sci
f1 = 1000
f2 = 2800
f3 = 3600
fs = 10000
dt = 1/fs
t = np.arange(0,15,dt)
t1 = np.arange(0, 5, dt)
t2 = np.arange(5, 10, dt)
t3 = np.arange(10, 15, dt)
p1 =  np.sin(2 * np.pi *f1* t1)
p2 = np.sin(2 * np.pi * f2 * t2) 
p3 = np.sin(2 * np.pi * f3 *t3)
p = np.concatenate([p1, p2, p3])
sci.write('sine_wave2.wav', 10000, p)
plt.title('wave')
plt.plot(p)
plt.show()
spect = lib.stft(p, n_fft = 2048, hop_length= 512)
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

