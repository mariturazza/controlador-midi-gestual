import rtmidi
from config.config import MIDI_PORT_NAME

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if MIDI_PORT_NAME in available_ports:
    midiout.open_port(available_ports.index(MIDI_PORT_NAME))
    print(f"Porta MIDI conectada: {MIDI_PORT_NAME}")
else:
    raise RuntimeError("Porta MIDI não encontrada.")

nota_atual = {'right': None, 'left': None}

def send_note_on(note, hand, velocity, canal):
    if nota_atual[hand]:
        midiout.send_message([0x80 | canal, nota_atual[hand], 0])
    midiout.send_message([0x90 | canal, note, velocity])
    nota_atual[hand] = note

def send_note_off(hand, canal):
    if nota_atual[hand]:
        midiout.send_message([0x80 | canal, nota_atual[hand], 0])
        nota_atual[hand] = None

def send_cc(controller, value):
    midiout.send_message([0xB0, controller, value])

def close_midi():
    midiout.close_port()
