from controller.loops import start_loop, stop_loop
from config.config import canais, escalas
from controller.midi_controller import send_note_on, send_note_off

def processar_mao_criativo(dedos, velocity, lado, config):
    instrumento_nome = config["instrumento"]
    escala_nome = config["escala"]
    canal = canais[instrumento_nome]
    escala = escalas[instrumento_nome][escala_nome]

    global estado_anterior

    if instrumento_nome == 'bateria':
        dedos_para_notas = {
            (1, 1, 1, 1, 1): escala[0],
            (0, 1, 1, 1, 1): escala[1],
            (0, 1, 1, 1, 0): escala[2],
            (0, 1, 1, 0, 0): escala[3],
            (0, 1, 0, 0, 0): escala[4],
            (1, 1, 0, 0, 0): escala[5],
            (1, 1, 0, 0, 1): escala[6]
        }

        dedos_tuple = tuple(dedos)
        if dedos_tuple != estado_anterior[lado]:
            estado_anterior[lado] = dedos_tuple
            if dedos_tuple in dedos_para_notas:
                send_note_on(dedos_para_notas[dedos_tuple], lado, velocity, canal)
            else:
                send_note_off(lado, canal)

    else:
        notas_por_dedos = [
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1]
        ]
        for i, config_dedos in enumerate(notas_por_dedos):
            if dedos == config_dedos:
                send_note_on(escala[i], lado, velocity, canal)
                return
        send_note_off(lado, canal)
        stop_loop(lado.capitalize())

def processar_mao_recreativo_loop(dedos, velocity, lado, config):
    instrumento_nome = config["instrumento"]
    canal = canais[instrumento_nome]
    loop = config["loop"]
    
    global estado_anterior

    dedos_tuple = tuple(dedos)

    if dedos_tuple != estado_anterior[lado]:
        estado_anterior[lado] = dedos_tuple

        if dedos_tuple == (1, 1, 1, 1, 1):
            if instrumento_nome == 'bateria':
                start_loop(lado, loop, velocity, canal)
            else:
                start_loop(lado, loop, velocity, canal)
            return

        if dedos_tuple == (1, 1, 1, 1, 0):
            stop_loop(lado)
            send_note_off(lado, canal)
            return

        send_note_off(lado, canal)
        stop_loop(lado.capitalize())

def processar_mao_recreativo_notas(dedos, velocity, lado, config):
    instrumento_nome = config["instrumento"]
    escala_nome = config["escala"]
    canal = canais[instrumento_nome]
    escala = escalas[instrumento_nome][escala_nome]

    global estado_anterior

    if instrumento_nome == 'bateria':
        dedos_para_notas = {
            (1, 1, 1, 1, 1): escala[0],
            (0, 1, 1, 1, 1): escala[1],
            (0, 1, 1, 1, 0): escala[2],
            (0, 1, 1, 0, 0): escala[3],
            (0, 1, 0, 0, 0): escala[4],
            (1, 1, 0, 0, 0): escala[5],
            (1, 1, 0, 0, 1): escala[6]
        }

        dedos_tuple = tuple(dedos)
        if dedos_tuple != estado_anterior[lado]:
            estado_anterior[lado] = dedos_tuple
            if dedos_tuple in dedos_para_notas:
                send_note_on(dedos_para_notas[dedos_tuple], lado, velocity, canal)
            else:
                send_note_off(lado, canal)

    else:
        notas_por_dedos = [
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1]
        ]
        for i, config_dedos in enumerate(notas_por_dedos):
            if dedos == config_dedos:
                send_note_on(escala[i], lado, velocity, canal)
                return
        send_note_off(lado, canal)
        stop_loop(lado.capitalize())
        
estado_anterior = {
    'right': None,
    'left': None
}