import board
import digitalio
import analogio
import rotaryio
import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
import adafruit_matrixkeypad

MIDI_CH = 1  # 2 for second deck
THRESHOLD = 2

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=MIDI_CH - 1)

s_pins = [
    digitalio.DigitalInOut(p) for p in (board.GP2, board.GP3, board.GP4, board.GP5)
]
for p in s_pins:
    p.switch_to_output()
mux_adc = analogio.In(board.GP26)
last_analog = [0] * 5


def get_mux(ch):
    for i in range(4):
        s_pins[i].value = (ch >> i) & 1
    return mux_adc.value >> 9


rows = [
    digitalio.DigitalInOut(x)
    for x in (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20)
]
cols = [
    digitalio.DigitalInOut(x) for x in (board.GP12, board.GP13, board.GP14, board.GP15)
]
keys = range(20)
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
last_keys = set()

encs = [
    rotaryio.IncrementalEncoder(board.GP6, board.GP7),
    rotaryio.IncrementalEncoder(board.GP8, board.GP9),
    rotaryio.IncrementalEncoder(board.GP10, board.GP11),
]
last_enc_pos = [0, 0, 0]

while True:
    for i in range(5):
        val = get_mux(i)
        if abs(val - last_analog[i]) >= THRESHOLD:
            midi.send(ControlChange(20 + i, val))
            last_analog[i] = val

    cur_keys = set(keypad.pressed_keys)
    for k in cur_keys - last_keys:
        midi.send(NoteOn(30 + k, 127))
    for k in last_keys - cur_keys:
        midi.send(NoteOff(30 + k, 0))
    last_keys = cur_keys

    for i in range(3):
        pos = encs[i].position
        if pos != last_enc_pos[i]:
            msg = 127 if pos > last_enc_pos[i] else 1
            midi.send(ControlChange(40 + i, msg))
            last_enc_pos[i] = pos
