import librosa as lib
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as sci
f1 = 1000
f2 = 2800
f3 = 3600
fs = 25000
dt = 1/fs
t = np.arange(0, 30, dt)
u1 = np.arange(0,1)
def unit_step(a,b, n):
    unit =[]
    for sample in n:
        if sample<a:
            unit.append(0)
        else:
            if sample>b:
                unit.append(0)
            else:
                unit.append(1)
    return(unit) 
u1 = unit_step(0 , 10 ,t) 
u2 = unit_step(10, 20, t)
u3 = unit_step(20, 30, t)
p1 =  u1 * (np.sin(2 * np.pi *f1* t))
p2 = u2 * (np.sin(2 * np.pi * f2 * t) )
p3 = u3 * (np.sin(2 * np.pi * f3 *t))
p = p1 + p2 + p3
sci.write('sine_wave.wav', 44100, p)
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
Created on Fri Jun 11 19:09:34 2021

@author: Admin
"""

