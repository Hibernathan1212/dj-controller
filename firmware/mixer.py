import board
import digitalio
import analogio
import usb_midi
import adafruit_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

MIDI_CH = 3
ANALOG_THRESHOLD = 2

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=MIDI_CH - 1)

s_pins = [
    digitalio.DigitalInOut(p) for p in (board.GP2, board.GP3, board.GP4, board.GP5)
]
for p in s_pins:
    p.switch_to_output()

mux1_adc = analogio.AnalogIn(board.GP26)
mux2_adc = analogio.AnalogIn(board.GP27)

last_mux1 = [0] * 16
last_mux2 = [0] * 9

cue_pins = (board.GP14, board.GP15, board.GP16, board.GP17)
cue_buttons = []
for p in cue_pins:
    btn = digitalio.DigitalInOut(p)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    cue_buttons.append(btn)
last_cue_state = [True] * 4

while True:
    for i in range(16):
        for bit in range(4):
            s_pins[bit].value = (i >> bit) & 1

        m1_val = mux1_adc.value >> 9
        if abs(m1_val - last_mux1[i]) >= ANALOG_THRESHOLD:
            midi.send(ControlChange(50 + i, m1_val))
            last_mux1[i] = m1_val
        if i < 9:
            m2_val = mux2_adc.value >> 9
            if abs(m2_val - last_mux2[i]) >= ANALOG_THRESHOLD:
                midi.send(ControlChange(70 + i, m2_val))
                last_mux2[i] = m2_val

    for i in range(4):
        cur_state = cue_buttons[i].value
        if cur_state != last_cue_state[i]:
            if not cur_state:
                midi.send(NoteOn(10 + i, 127))
            else:
                midi.send(NoteOff(10 + i, 0))
            last_cue_state[i] = cur_state
