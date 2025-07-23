import cv2
import json

from camera.camera import process_frame, draw_hand
from hand.detection import detectar_dedos, altura_mao
from controller.midi_controller import send_note_on, send_note_off, close_midi
from controller.loops import start_loop, stop_loop, loop_flags
from config.config import notas_guitarra, escalas

dados_maos_json = '''{
  "Right": {
    "instrumento": "bateria",
    "escala": "bateria 1"
  },
  "Left": {
    "instrumento": "piano",
    "escala": "pentatonica maior de DO"
  }
}'''

dados = json.loads(dados_maos_json)

canais = {
  "bateria": 0,
  "piano": 1
}

estado_anterior = {
    'right': None,
    'left': None
}

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

                    if hand_label == 'Right':
                        
                        instrumento_right = dados["Right"]["instrumento"]
                        canal_direito = canais[instrumento_right]
                        
                        escala_right = dados["Right"]["escala"]
                        escala = escalas[escala_right]
                        
                        hand = 'right'
                        
                        if instrumento_right == 'bateria':
                            
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

                            # verifica se houve mudança no gesto
                            if dedos_tuple != estado_anterior['right']:
                                estado_anterior['right'] = dedos_tuple

                                if dedos_tuple in dedos_para_notas:
                                    nota = dedos_para_notas[dedos_tuple]
                                    send_note_on(nota, 'right', velocity, canal_direito)
                                else:
                                    send_note_off('right', canal_direito)
                        
                        else:
                            
                            if dedos == [1, 1, 1, 1, 1]:
                                send_note_on(escala[0], hand, velocity, canal_direito)
                                
                            elif dedos == [0, 1, 1, 1, 1]:
                                send_note_on(escala[1], hand, velocity, canal_direito)
                            
                            elif dedos == [0, 1, 1, 1, 0]:
                                send_note_on(escala[2], hand, velocity, canal_direito)
                            
                            elif dedos == [0, 1, 1, 0, 0]:
                                send_note_on(escala[3], hand, velocity, canal_direito)
                            
                            elif dedos == [0, 1, 0, 0, 0]:
                                send_note_on(escala[4], hand, velocity, canal_direito)
                            
                            elif dedos == [1, 1, 0, 0, 0]:
                                send_note_on(escala[5], hand, velocity, canal_direito)
                            
                            elif dedos == [1, 1, 0, 0, 1]:
                                send_note_on(escala[6], hand, velocity, canal_direito)
                            
                            else:
                                send_note_off(hand, canal_direito)
                                stop_loop(hand_label)
                    
                    elif hand_label == 'Left':
                        
                        instrumento_left = dados["Left"]["instrumento"]
                        canal_esquerdo = canais[instrumento_left]
                        
                        escala_left = dados["Left"]["escala"]
                        escala = escalas[escala_left]
                        
                        hand = 'left'
                        
                        if instrumento_left == 'bateria':
                            
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

                            # verifica se houve mudança no gesto
                            if dedos_tuple != estado_anterior['left']:
                                estado_anterior['left'] = dedos_tuple

                                if dedos_tuple in dedos_para_notas:
                                    nota = dedos_para_notas[dedos_tuple]
                                    send_note_on(nota, 'left', velocity, canal_esquerdo)
                                else:
                                    send_note_off('left', canal_esquerdo)
                        
                        else:
                            
                            if dedos == [1, 1, 1, 1, 1]:
                                send_note_on(escala[0], hand, velocity, canal_esquerdo)
                                
                            elif dedos == [0, 1, 1, 1, 1]:
                                send_note_on(escala[1], hand, velocity, canal_esquerdo)
                            
                            elif dedos == [0, 1, 1, 1, 0]:
                                send_note_on(escala[2], hand, velocity, canal_esquerdo)
                            
                            elif dedos == [0, 1, 1, 0, 0]:
                                send_note_on(escala[3], hand, velocity, canal_esquerdo)
                            
                            elif dedos == [0, 1, 0, 0, 0]:
                                send_note_on(escala[4], hand, velocity, canal_esquerdo)
                            
                            elif dedos == [1, 1, 0, 0, 0]:
                                send_note_on(escala[5], hand, velocity, canal_esquerdo)
                            
                            elif dedos == [1, 1, 0, 0, 1]:
                                send_note_on(escala[6], hand, velocity, canal_esquerdo)
                            
                            else:
                                send_note_off(hand, canal_esquerdo)
                                stop_loop(hand_label)

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

if __name__ == "__main__":
    main()
