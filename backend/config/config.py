#    'DO': 60, 'RE': 62, 'MI': 64, 'FA': 65,
#    'SOL': 67, 'LA': 69, 'SI': 71, 'DO_8': 72

MIDI_PORT_NAME = "loopMIDI Port 1"
BPM = 186

canais = {
    "bateria": 0,
    "teclado": 1,
    "guitarra": 2
}

escalas = {
    "bateria": {
        "1": [36, 42, 38, 46, 43, 45, 49],
        "2": [36, 42, 38, 46, 43, 45, 49],
        "3": [36, 42, 38, 46, 43, 45, 49],
        "Seven Nation Army": [36, 0, 0, 0, 0, 0, 0]
    },
    "teclado": {
        "1": [60, 62, 64, 67, 69, 72, 74], #pentatonica de do
        "2": [60, 62, 64, 65, 67, 69, 71, 72], #maior de do
        "3": [60, 62, 64, 65, 67, 69, 71, 72]
    },
    "guitarra": {
        "1": [60, 62, 64, 67, 69, 72, 74],
        "2": [60, 62, 64, 65, 67, 69, 71, 72],
        "3": [60, 62, 64, 65, 67, 69, 71, 72],
        "Seven Nation Army": [67, 64, 62, 60, 59, 0, 0]
    }
};

musicas = {
    "Seven Nation Army": {
        "Right": 
            {"instrumento": "bateria", "escala": "Seven Nation Army"}, 
        "Left": 
            {"instrumento": "guitarra", "escala": "Seven Nation Army"}
        }
}