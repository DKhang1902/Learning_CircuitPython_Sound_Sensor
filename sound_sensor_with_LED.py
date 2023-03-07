import audiobusio
import array
import board
import math
import time
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.1)


def mean(values):
    return sum(values)/len(values)

def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(float(sample - minbuf) * (sample-minbuf) for sample in values)
    return math.sqrt(samples_sum / len(values))

def reset_pixels():
    pixels.fill((0,0,0))
    pixels.show()

def light_up(pixel_num):
    pixel_num = magnitude // 60
    if pixel_num > 10:
        pixel_num = 10
    for i in range(pixel_num):
        pixels[i] = (255,255,255)
        pixels.show()
    

mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA, sample_rate= 16000, bit_depth=16)
samples = array.array("H",[0]*160)

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    light_up(magnitude)
    reset_pixels()
    print(magnitude)
    
