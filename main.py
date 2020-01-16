import pretty_midi
import math

# Settings ----------------

# length in secs
audio_len = 5
# resolution in hz
audio_res = 5

# output dimensions = (len*res)^2

# Settings ----------------


midi_data = pretty_midi.PrettyMIDI('midi_downloads/mario.mid')
num_inst = len(midi_data.instruments)

def discretize(input_time):
    second = math.floor(input_time) if (math.floor(input_time)<= audio_len) else audio_len
    remainder = input_time % 1
    sector = 0

    for x in range(0, audio_res):
        # print((1 / audio_res) * x)
        if (remainder >= (1 / audio_res) * x):
            sector = x

    return second * audio_res + sector


print(discretize(1.75))

for inst_index in range (0, num_inst):
    instrument = midi_data.instruments[inst_index]
    print("inst"+str(inst_index))
    for note_index in range (0, len(instrument.notes) - 1):
        if (instrument.notes[note_index].start< audio_len):
            print([instrument.notes[note_index]])
        else:
            break


# print(midi_data.instruments[0].notes)