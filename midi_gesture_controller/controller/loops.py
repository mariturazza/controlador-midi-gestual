import threading
import time
from controller.midi_controller import send_note_on, send_note_off
from config.config import BPM

loop_flags = {'right': False, 'left': False}

def loop_drum(hand, velocity, canal):
    notas_loop = [[42, 36], [42], [42, 38], [42, 36], [42], [42], [42, 38], [42, 36]]
    duracoes = [0.5]*8
    beat_time = 60 / BPM

    for notas, dur in zip(notas_loop, duracoes):
        for nota in notas:
            send_note_on(nota, hand, velocity, canal)
        time.sleep(dur * beat_time)
        for nota in notas:
            send_note_off(hand, canal)

def loop_bass(hand, velocity, canal):
    notas = [48, 45, 47, 40]
    loop_flags[hand] = True
    indice = 0
    beat_time = 60 / BPM
    padrao = [1, None, 1, None, 1, None, 1, None, 1, None, 1, None]
    duracoes = [0.8, 0.2, 0.3, 0.2, 0.8, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3, 0.2]

    while loop_flags[hand]:
        for flag, dur in zip(padrao, duracoes):
            if not loop_flags[hand]:
                break
            if flag:
                send_note_on(notas[indice], hand, velocity, canal)
            time.sleep(dur * beat_time)
            if flag:
                send_note_off(hand, canal)
        indice = (indice + 1) % len(notas)

    send_note_off(hand, canal)

def start_loop(hand, tipo, velocity, canal):
    if tipo == 'drum':
        thread = threading.Thread(target=loop_drum, args=(hand, velocity, canal))
    else:
        thread = threading.Thread(target=loop_bass, args=(hand, velocity, canal))
    loop_flags[hand] = True
    thread.start()

def stop_loop(hand):
    loop_flags[hand] = False
