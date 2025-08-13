#    'DO': 60, 'RE': 62, 'MI': 64, 'FA': 65,
#    'SOL': 67, 'LA': 69, 'SI': 71, 'DO_8': 72

MIDI_PORT_NAME = "loopMIDI Port 1"

canais = {
    "bateria": 0, #channel 1
    "teclado": 1, #channel 2
    "guitarra": 2 #channel 3
}

escalas = {
    "bateria": {
        "1": [36, 42, 38, 46, 43, 45, 49],
        "2": [36, 42, 38, 46, 43, 45, 49],
        "3": [36, 42, 38, 46, 43, 45, 49],
        "Seven Nation Army": [36, 0, 0, 0, 0, 0, 0],
        "Billie Jean": [36, 42, 38, 0, 0, 0, 0]
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
        "Seven Nation Army": [67, 64, 62, 60, 59, 0, 0],
        "Billie Jean": [54, 49, 52, 47, 0, 0, 0]
    }
};

musicas = {
    "Seven Nation Army": {
        "facil": {
            "Right": 
                {"instrumento": "bateria", "loop": "Seven Nation Army Drum"}, 
            "Left": 
                {"instrumento": "guitarra", "loop": "Seven Nation Army Bass"}
        },
        "dificil": {
           "Right": 
                {"instrumento": "bateria", "escala": "Seven Nation Army"}, 
            "Left": 
                {"instrumento": "guitarra", "escala": "Seven Nation Army"} 
        }
    },
    "Billie Jean": {
        "facil": {
            "Right": 
                {"instrumento": "bateria", "loop": "Billie Jean Drum"}, 
            "Left": 
                {"instrumento": "guitarra", "loop": "Billie Jean Bass"}
        },
        "dificil": {
           "Right": 
                {"instrumento": "bateria", "escala": "Billie Jean"}, 
            "Left": 
                {"instrumento": "guitarra", "escala": "Billie Jean"} 
        }
    }
}