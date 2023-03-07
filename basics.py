import audiobusio
import array
import board
import math
import time


def mean(values):
    return sum(values)/len(values)

def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(float(sample - minbuf) * (sample-minbuf) for sample in values)
    return math.sqrt(samples_sum / len(values))



mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate= 16000, bit_depth=16)
samples = array.array("H",[0]*160)

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print(magnitude)
