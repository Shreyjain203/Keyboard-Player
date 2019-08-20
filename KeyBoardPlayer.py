import numpy as np
import sounddevice as sd
import msvcrt
sd.default.samplerate = 44100

time = 0.25
frq = 150

def gen_Sound(frq):
    samples = np.arange(44100* time)/44100.0
    wave = 10000 * np.sin(2*np.pi * frq * samples)
    wav_wave = np.array(wave,dtype = np.int16)
    sd.play(wav_wave, blocking = True)


#while True:
#    a = ord(msvcrt.getch())
#    gen_Sound(5*a + a*15)
    
    
while True:
    a = ord(msvcrt.getch())-10
    b= (2**(1/12))**(a-49)
    gen_Sound(b*frq)
    

