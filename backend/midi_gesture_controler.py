import cv2
import json

from camera.camera import process_frame, draw_hand

from hand.detection import detectar_dedos, altura_mao

from controller.midi_controller import send_note_on, send_note_off, close_midi
from controller.loops import start_loop, stop_loop
from config.config import canais, escalas

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
        
def processar_mao_recriativo(dedos, velocity, lado, config):
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

def main():
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results, image = process_frame(frame)

            if results.multi_hand_landmarks and results.multi_handedness:
                for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    hand_label = results.multi_handedness[idx].classification[0].label
                    draw_hand(image, hand_landmarks)
                    dedos = detectar_dedos(hand_landmarks, hand_label)
                    altura = altura_mao(hand_landmarks)
                    velocity = int((1 - altura) * 127)
                    
                    modo = list(dados.keys())[0]

                    if modo == 'criativo':
                        if hand_label == 'Right':
                            processar_mao_criativo(dedos, velocity, 'right', dados[modo]["Right"])
                        elif hand_label == 'Left':
                            processar_mao_criativo(dedos, velocity, 'left', dados[modo]["Left"])
                    else:
                        if hand_label == 'Right':
                            processar_mao_recreativo(dedos, velocity, 'right', dados[modo]["Right"])
                        elif hand_label == 'Left':
                            processar_mao_recreativo(dedos, velocity, 'left', dados[modo]["Left"])
                            
            else:
                send_note_off('right', 0)
                send_note_off('left', 9)

            cv2.imshow("Controlador MIDI por Gestos", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        send_note_off('right', 0)
        send_note_off('left', 9)
        close_midi()
        cap.release()
        cv2.destroyAllWindows()

with open('dados.json', 'r') as f:
    dados = json.load(f)

estado_anterior = {
    'right': None,
    'left': None
}

if __name__ == "__main__":
    main()
