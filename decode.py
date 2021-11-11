import sounddevice as sd
import soundfile as sf # Não estava conseguindo importar esse soundfile
import matplotlib.pyplot as plt
from scipy import signal
from suaBibSignal import signalMeu
from funcoes_LPF import *

signal = signalMeu()
fs = 44100

sd.default.samplerate = fs
sd.default.channels = 1

reader = sf.read("file.wav")
file = reader[0]

t = len(file) / fs

portadora = 14e3

portadoraT, portadoraY = signal.generateSin(portadora, 1, t, fs)
demodulated_signal =  [x / y if y else 0 for x,y in zip(file, portadoraY)]

band_amplitude = 4e3
arquivo_filtrado = LPF(demodulated_signal, band_amplitude, fs)

sd.play(arquivo_filtrado)
sd.wait()

signal.plotFFT(demodulated_signal, fs)
signal.plotFFT(demodulated_signal, fs)
plt.show()