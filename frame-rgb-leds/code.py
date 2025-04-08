import board
import neopixel

pixels = neopixel.NeoPixel(board.D0, 10)

while True:
  for r in range(0, 255):
    for g in range(0, 255):
      for b in range(0, 255):
        pixels.fill((r, g, b))
