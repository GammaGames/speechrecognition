from pydub import AudioSegment
import speech_recognition as sr
import math
import os
import shutil
import sys

if len(sys.argv) == 1:
	print('Use: python3 sr.py <file> <length>*')
	quit()
file = sys.argv[1]
if len(sys.argv) == 3:
	length = int(sys.argv[2]) * 1000
else:
	length = 30000
r = sr.Recognizer()
folder = file.split('/')[-1].split('.')[0]
filetype = file.split('/')[-1].split('.')[-1]

sound = AudioSegment.from_wav(file)
numClips = math.floor(len(sound) / length)
if os.path.exists(folder):
	shutil.rmtree(folder)
os.makedirs(folder)

for x in range(0, numClips):
	clip = sound[x * length:(x + 1) * length]
	clip.export(folder + '/' + str(x) + '.' + filetype, format=filetype)

f = open(folder + '/output.txt', 'w+')

for x in range(0, numClips):
	print(str(x) + '/' + str(numClips))
	clip = sr.AudioFile(folder + '/' + str(x) + '.' + filetype)
	with clip as source:
		audio = r.record(source)
	f.write(str(x) + '.' + filetype + '\r\n')
	try:
		f.write(r.recognize_google(audio))
	except sr.UnknownValueError:
		f.write('Unrecognizable audio')
	f.write('\r\n')

f.close()
