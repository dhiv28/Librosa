import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
y = lib.tone(440, sr=22050, length=22050)
plt.plot(y[2000:2100])
plt.show()
spect = lib.stft(y, n_fft = 2048, hop_length= 512)
spect_db = lib.amplitude_to_db(np.abs(spect))
librosa.display.specshow(spect_db, x_axis ='time', y_axis='log')
plt.title('spectrogram')
plt.colorbar()
plt.show()
"""
Created on Sat Jun  5 11:35:07 2021

@author: Admin
"""

