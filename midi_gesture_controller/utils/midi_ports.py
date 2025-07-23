import rtmidi

def listar_portas_midi():
    midiout = rtmidi.MidiOut()
    ports = midiout.get_ports()
    print("Portas MIDI disponíveis:")
    for i, port in enumerate(ports):
        print(f"{i}: {port}")
    midiout.close_port()
