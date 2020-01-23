import sys
import pretty_midi
import math
import random
from PIL import Image, ImageDraw

# Settings ----------------
filename = 'images/testWil1.png'
if (len(sys.argv) > 1):
    filename = sys.argv[1]

# The resolution and the tick scales are given in the default pretty midi file
# Unless resolution is specified in the Setting
resolution = -1
if (len(sys.argv) > 2):
    resolution = int(sys.argv[2])

tick_duration = -1
if (len(sys.argv) > 3):
    tick_duration = float(sys.argv[3])

pixel_res = 8
if (len(sys.argv) > 4):
    pixel_res = int(sys.argv[4])
# Settings ----------------


midi_data = pretty_midi.PrettyMIDI()
resolution = midi_data.resolution if resolution == -1 else resolution# how many ticks in a beat
tick_duration = midi_data._tick_scales[0][1] if tick_duration == -1 else tick_duration# Get tick duration from the first tempo signature - we assume the tempo to be uniform
audio_res = resolution / pixel_res * tick_duration # how long in seconds does a pixel lasts

midi_data.resolution = resolution
midi_data._tick_scales[0] = (midi_data._tick_scales[0][0], tick_duration)
img = Image.open(filename)
x, y = img.size

for y_iter in range(y):
    # Create Instrument
    inst_prog = pretty_midi.instrument_name_to_program('Cello')
    instm = pretty_midi.Instrument(program=inst_prog)

    # Start reading the note image file
    x_iter = 0
    while (x_iter < x):
        pix = img.getpixel((x_iter, y_iter))  
        pitch = pix[0] # TODO: change this scheme if note mapping changes
        start_time = x_iter * audio_res # start time with pixel resolution

        if (pitch != 0):
            # Note found
            # Loop through x_iter until the current pitch ends
            while (x_iter < x and img.getpixel((x_iter, y_iter))[0] == pitch):
                x_iter += 1

            end_time = x_iter * audio_res
            print((pitch, start_time, end_time))     
            note = pretty_midi.Note(velocity=100, pitch=(pitch - 24), start=start_time, end=end_time)
            instm.notes.append(note)

            x_iter -= 1

        x_iter += 1
        
    midi_data.instruments.append(instm)

midi_data.write("midi_outputs/output.mid")