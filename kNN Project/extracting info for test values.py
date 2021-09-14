import librosa
import numpy

#Load song
y, sr = librosa.load('Radio Ga Ga.wav')

#Extract features using Librosa
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
stft = librosa.feature.chroma_stft(y=y, sr=sr)
rms = librosa.feature.rms(y=y)
spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
roll_off = librosa.feature.spectral_rolloff(y=y, sr=sr)
zero_crossing_rate = librosa.feature.zero_crossing_rate(y=y)

#Find average
stft = numpy.mean(stft)
rms = numpy.mean(rms)
spectral_centroid = numpy.mean(spectral_centroid)
spectral_bandwidth = numpy.mean(spectral_bandwidth)
roll_off = numpy.mean(roll_off)
zero_crossing_rate = numpy.mean(zero_crossing_rate)

#Print values
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
print('STFT:', stft)
print('RMS:', rms)
print('Spectral centroid:', spectral_centroid)
print('Spectral bandwidth:', spectral_bandwidth)
print('Roll-off:', roll_off)
print('Zero crossing rate:', zero_crossing_rate)
