import time
from RPLCD.i2c import CharLCD
import mpmath

LCD_ADDR = 0x27

lcd = CharLCD(
    i2c_expander='PCF8574',
    address=LCD_ADDR,
    port=1,
    cols=20,
    rows=4,
    charmap='A00'
)

# -------- Custom characters --------

confetti_1 = [
    0b00000,
    0b00100,
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b10001,
    0b00100,
]

confetti_2 = [
    0b00000,
    0b01010,
    0b00100,
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b00000,
]

# DOWN arrow (points at numbers below it)
down_arrow = [
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b00100,
    0b10101,
    0b01110,
    0b00100,
]

lcd.create_char(0, confetti_1)
lcd.create_char(1, confetti_2)
lcd.create_char(2, down_arrow)

# -------- Pi string --------
mpmath.mp.dps = 5000
pi_str = str(mpmath.pi)  # includes "3."

ARROW_COL = 0  # change this if you want arrow under a different column

def draw_header():
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Happy Pi Day :)".ljust(20))

def draw_display(start_index, digit_count):
    # Line 2 — counter (dot not counted)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(f"Pi Digit: {digit_count:06d}".ljust(20))

    # Line 3 — arrow
    lcd.cursor_pos = (2, 0)
    lcd.write_string((" " * ARROW_COL + "\x02").ljust(20))

    # Line 4 — scrolling π numbers
    chunk = pi_str[start_index:start_index + 20]
    if len(chunk) < 20:
        chunk += pi_str[:20 - len(chunk)]
    lcd.cursor_pos = (3, 0)
    lcd.write_string(chunk)

def celebration_flash():
    for k in range(6):
        frame = "\x00" if (k % 2 == 0) else "\x01"
        lcd.cursor_pos = (0, 0)
        lcd.write_string(("HAPPY PI DAY! " + frame + frame).ljust(20))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("3.141592653589793".ljust(20))
        time.sleep(0.2)
        lcd.cursor_pos = (0, 0)
        lcd.write_string(" " * 20)
        lcd.cursor_pos = (1, 0)
        lcd.write_string(" " * 20)
        time.sleep(0.2)

    lcd.clear()
    draw_header()

# -------- Start --------

lcd.clear()
draw_header()

start_index = 0
digit_count = 0

while True:

    # Current character under arrow
    current_index = (start_index + ARROW_COL) % len(pi_str)
    current_char = pi_str[current_index]

    # Celebrate every 100 digits (not counting dot)
    if digit_count != 0 and digit_count % 100 == 0:
        celebration_flash()

    draw_display(start_index, digit_count)

    # Scroll forward
    start_index = (start_index + 1) % len(pi_str)

    # Increase counter only if digit
    if current_char.isdigit():
        digit_count += 1

    # Reset at full wrap
    if start_index == 0:
        digit_count = 0

    time.sleep(1)
