import cv2
import json

from camera.camera import process_frame, draw_hand
from hand.detection import detectar_dedos, altura_mao
from controller.midi_controller import send_note_off, close_midi
from config.config import musicas
from services.hand_process import processar_mao_criativo, processar_mao_recreativo_loop, processar_mao_recreativo_notas

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
                    
                    elif modo == 'recreativo':    
                        faixa = musicas[dados['recreativo']['musica']]                    
                        dificuldade = dados['recreativo']['dificuldade']      
                        
                        if dificuldade == 'facil':
                            if hand_label == 'Right':
                                processar_mao_recreativo_loop(dedos, velocity, 'right', faixa["facil"]["Right"])
                            elif hand_label == 'Left':
                                processar_mao_recreativo_loop(dedos, velocity, 'left', faixa["facil"]["Left"])
                            
                        elif dificuldade == 'medio':
                            if hand_label == 'Right':
                                processar_mao_recreativo_loop(dedos, velocity, 'right', faixa["facil"]["Right"])
                            elif hand_label == 'Left':
                                processar_mao_recreativo_notas(dedos, velocity, 'left', faixa["dificil"]["Left"])
                            
                        elif dificuldade == 'dificil':
                            if hand_label == 'Right':
                                processar_mao_recreativo_notas(dedos, velocity, 'right', faixa["dificil"]["Right"])
                            elif hand_label == 'Left':
                                processar_mao_recreativo_notas(dedos, velocity, 'left', faixa["dificil"]["Left"])
                                
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

if __name__ == "__main__":
    main()
