import soundfile as sf
import sounddevice as sd
data,fs=sf.read("sound/lofi1.mp3")
print("sound playing...")
sd.play(data,fs)
sd.wait()
print("done")