import board
import neopixel

pixels = neopixel.NeoPixel(board.D0, 10)

print("starting pixels")
while True:
  for rgb in range(0, 255):
    pixels.fill((rgb, rgb, rgb))
    pixels.show()
    print(f"duhhrhrh rgb: {rgb}")
