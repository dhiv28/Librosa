import librosa as lib
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
x = np.arange (-4*np.pi, 4*np.pi , 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
spect = lib.stft(y, n_fft = 2048, hop_length= 512)
spect_db = lib.amplitude_to_db(np.abs(spect))
librosa.display.specshow(spect_db, x_axis ='time', y_axis='log')
plt.title('spectrogram')
plt.colorbar()
plt.show()



"""
Spyder Editor

This is a temporary script file.
"""

