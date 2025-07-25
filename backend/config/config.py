#    'DO': 60, 'RE': 62, 'MI': 64, 'FA': 65,
#    'SOL': 67, 'LA': 69, 'SI': 71, 'DO_8': 72

MIDI_PORT_NAME = "loopMIDI Port 1"
BPM = 186

app_data_criativo = {
    "instrumentos": {
        "bateria": {
            "escalas": [
                "bateria 1",
                "bateria 2"
            ]
        },
        "teclado" : {
            "escalas": [
                "pentatonica maior de DO",
                "escala maior de DO"
            ]
        },
        "guitarra" : {
            "escalas": [
                "pentatonica maior de DO", 
                "escala maior de DO"
            ]
        }
    }
}

canais = {
    "bateria": 0,
    "teclado": 1,
    "guitarra": 2
}

escalas = {
    "bateria 1": [36, 42, 38, 46, 43, 45, 49],
    "bateria 2": [36, 42, 38, 46, 43, 45, 49],
    "pentatonica maior de DO": [60, 62, 64, 67, 69, 72, 74],
    "escala maior de DO": [60, 62, 64, 65, 67, 69, 71, 72],
    "pentatonica maior de DO": [60, 62, 64, 67, 69, 72, 74],
    "escala maior de DO": [60, 62, 64, 65, 67, 69, 71, 72]
}