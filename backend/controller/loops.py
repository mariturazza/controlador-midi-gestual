import threading
import time
from controller.midi_controller import send_note_on, send_note_off

loop_flags = {'right': False, 'left': False}

def loop_drum_seven_nation_army(hand, velocity, canal):
    notas_loop = [[36], [36], [36], [36], [36], [36], [36], [36]]
    duracoes = [1]*16
    beat_time = 60 / 104

    for notas, dur in zip(notas_loop, duracoes):
        for nota in notas:
            send_note_on(nota, hand, velocity, canal)
        time.sleep(dur * beat_time)
        for nota in notas:
            send_note_off(hand, canal)

def loop_bass_seven_nation_army(hand, velocity, canal):
    notas_loop = [[64], [64], [67], [64], [62], [60], [59]]
    duracoes = [1.5, 0.5, 0.75, 0.75, 0.5, 2, 2]
    beat_time = 60 / 104
    
    for notas, dur in zip(notas_loop, duracoes):
        for nota in notas:
            send_note_on(nota, hand, velocity, canal)
        time.sleep(dur * beat_time)
        for nota in notas:
            send_note_off(hand, canal)

def start_loop(hand, loop, velocity, canal):
    if loop == "Seven Nation Army Drum":
        thread = threading.Thread(target=loop_drum_seven_nation_army, args=(hand, velocity, canal))
    
    elif loop == "Seven Nation Army Bass":
        thread = threading.Thread(target=loop_bass_seven_nation_army, args=(hand, velocity, canal))
    loop_flags[hand] = True
    thread.start()

def stop_loop(hand):
    loop_flags[hand] = False
