import sounddevice as sd
import soundfile as sf # Não estava conseguindo importar esse soundfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from suaBibSignal import SignalMeu
from funcoes_LPF import *

signal = SignalMeu()
fs = 44100 # Hz

file, sample_rate = sf.read("afew_modulado.wav")

signal = SignalMeu()
signal.fs = sample_rate
sd.default.samplerate = signal.fs
sd.default.channels = 1

lenSinal = len(file)
time = np.linspace(0, lenSinal/fs, lenSinal)
# time = len(file) / fs

freq_portadora = 14000 # Hz
portadora = np.cos(2*np.pi*freq_portadora*time)

demoduled = file*portadora

plt.title('Signal Demodulated')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(time, demoduled)
signal.plotFFT(demoduled, 'FFT Demodulated')

amplitude = 4000
filtered = filtro(demoduled, fs, amplitude)
signal.plotFFT(filtered, 'FFT Demodulated and Filtered')

sd.play(filtered, fs)
sd.wait()
plt.show()