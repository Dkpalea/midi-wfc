import sys
import pretty_midi
import math
import random
from PIL import Image, ImageDraw

# Settings ----------------

# length in secs
audio_len = 25
# how many pixels are in a beat
pixel_res = 8

filename = 'midi_downloads/bachStuff.mid'
if (len(sys.argv) > 1):
    filename = sys.argv[1]
    
output_filename = 'images/test.png'
if (len(sys.argv) > 2):
    filename = sys.argv[2]

# output dimensions = (len*res)^2

# Settings ----------------

midi_data = pretty_midi.PrettyMIDI(filename)

resolution = midi_data.resolution # how many ticks in a beat
tick_duration = midi_data._tick_scales[0][1] # Get tick duration from the first tempo signature - we assume the tempo to be uniform
audio_res = resolution / pixel_res * tick_duration # how long in seconds does a pixel lasts
num_inst = len(midi_data.instruments)

def discretize(input_time):

    #print("Resolution: " + str(resolution) + "; tick_duration: " + str(tick_duration) + "; audio_res: " + str(audio_res) )

    return math.floor(input_time / audio_res)

'''
    second = math.floor(input_time) if (math.floor(input_time)<= audio_len) else audio_len
    remainder = input_time % 1
    sector = 0

    for x in range(0, audio_res):
        # print((1 / audio_res) * x)
        if (remainder >= (1 / audio_res) * x):
            sector = x

    return second * audio_res + sector
'''


img = Image.new('RGB', (math.ceil(audio_len / audio_res), num_inst * 2), 'black')
idraw = ImageDraw.Draw(img)

for inst_index in range (0, num_inst - 1):
    instrument = midi_data.instruments[inst_index]
    #print("inst"+str(inst_index))
    for note_index in range (0, len(instrument.notes) - 1):
        if (instrument.notes[note_index].start< audio_len):
            #print([instrument.notes[note_index]])
            idraw.line([(discretize(instrument.notes[note_index].start), inst_index * 2),\
                        (discretize(instrument.notes[note_index].end), inst_index * 2)],\
                       (instrument.notes[note_index].pitch,random.randrange(0,255),255)\
                       )
        else:
            break


img.save('images/test.png')
print("[resolution, tick_duration, pixel_res]: " + str(resolution) + " " + str(tick_duration) + " " + str(pixel_res))

# print(midi_data.instruments[0].notes)