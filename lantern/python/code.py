import board
import neopixel
import time

NUM_PIXELS = 36

GRADIENT_DURATION = 4.0
MAX_RGB_VALUE = 255
TIME_BETWEEN_PULSES = 1.0

FLASH_HIGH_DURATION = 0.1
FLASH_LOW_DURATION = 1 - FLASH_HIGH_DURATION
PULSE_COUNT = 10
FLASH_COUNT = 4

pixels = neopixel.NeoPixel(board.GP0, NUM_PIXELS)


def do_pulse():
    pixels.fill((255, 255, 255))
    gradient_step_duration = GRADIENT_DURATION / 255
    for i in range(0, 255):
        pixels.brightness = 1.0 / 255 * i
        time.sleep(gradient_step_duration)
    for i in range(0, 255):
        pixels.brightness = 1.0 / 255 * (255 - i)
        time.sleep(gradient_step_duration)
        

def do_flash():
    pixels.fill((255, 255, 255))
    pixels.brightness = 1.0
    time.sleep(FLASH_HIGH_DURATION)
    pixels.brightness = 0
    time.sleep(FLASH_LOW_DURATION)


while True:
    for i in range(0, PULSE_COUNT):
        do_pulse()
        time.sleep(TIME_BETWEEN_PULSES)
    for i in range(0, FLASH_COUNT):
        do_flash()

