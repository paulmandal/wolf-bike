import board
import busio
import fourwire
import displayio
import gc9a01

TFT_WIDTH     = 240
TFT_HEIGHT    = 240
SQUARE_BORDER = 5

tft_clk = board.GP2
tft_mosi= board.GP3
tft_rst = board.GP26
tft_dc  = board.GP27
tft_cs  = board.GP1
tft_bl  = None

displayio.release_displays()
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)
display_bus = fourwire.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

main_display = displayio.Group()
display.root_group = main_display

color_bitmap = displayio.Bitmap(TFT_WIDTH, TFT_HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_display.append(bg_sprite)

inner_bitmap = displayio.Bitmap(TFT_WIDTH - SQUARE_BORDER * 2, TFT_HEIGHT - SQUARE_BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=SQUARE_BORDER, y=SQUARE_BORDER)
main_display.append(inner_sprite)


text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=28, y=HEIGHT // 2 - 1)
main_display.append(text_area)


while True:
    pass
