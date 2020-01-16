import pretty_midi
import math

# Settings ----------------

# length in secs
audio_len = 5
# how many pixels are in a beat
pixel_res = 8

# output dimensions = (len*res)^2

# Settings ----------------


midi_data = pretty_midi.PrettyMIDI('midi_downloads/mario.mid')
num_inst = len(midi_data.instruments)

def discretize(input_time):
    resoltuion = midi_data.resoltuion # how many ticks in a beat
    tick_duration = midi_data._tick_scales[0][1] # Get tick duration from the first tempo signature - we assume the tempo to be uniform
    audio_res = resolution / pixel_res * tick_duration # how long in seconds does a pixel lasts

    print("Resolution: " + str(resolution) + "; tick_duration: " + str(tick_duration) + "; audio_res: " + str(audio_res) )

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


print(discretize(1.75))

for inst_index  range (0, num_inst):
    instrument = midi_data.instruments[inst_index]
    print("inst"+stinr(inst_index))
    for note_index in range (0, len(instrument.notes) - 1):
        if (instrument.notes[note_index].start< audio_len):
            print([instrument.notes[note_index]])
        else:
            break


# print(midi_data.instruments[0].notes)