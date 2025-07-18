import cv2
import mediapipe as mp
import rtmidi
import time

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

desired_port = "python-to-lmms 1"

if desired_port in available_ports:
    midiout.open_port(available_ports.index(desired_port))
    print(f"Porta MIDI conectada: {desired_port}")
else:
    print("Porta MIDI não encontrada.")
    exit()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

notas = {
    'DO': 60,
    'RE': 62,
    'MI': 64,
    'FA': 65,
    'SOL': 67,
    'LA': 69,
    'SI': 71
}

nota_atual = None
efeito_autotune_ativo = False
batida_ativa = False

def send_note_on(note):
    global nota_atual
    if nota_atual is not None:
        midiout.send_message([0x80, nota_atual, 0])  
    midiout.send_message([0x90, note, 112])  
    nota_atual = note

def send_note_off():
    global nota_atual
    if nota_atual is not None:
        midiout.send_message([0x80, nota_atual, 0])
        nota_atual = None

def send_cc(controller, value):
    midiout.send_message([0xB0, controller, value])

def detectar_dedos(mao):
    dedos = []

    for i, tip_id in enumerate([4, 8, 12, 16, 20]):
        if tip_id == 4: 
            if mao.landmark[tip_id].x < mao.landmark[tip_id - 2].x:
                dedos.append(1)
            else:
                dedos.append(0)
        else:
            if mao.landmark[tip_id].y < mao.landmark[tip_id - 2].y:
                dedos.append(1)
            else:
                dedos.append(0)
    return dedos 

def altura_mao(mao):
    return mao.landmark[0].y 

cap = cv2.VideoCapture(0)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                dedos = detectar_dedos(hand_landmarks)
                altura = altura_mao(hand_landmarks)

                if dedos == [1, 1, 1, 1, 1]:
                    send_note_on(notas['DO'])
                elif dedos == [0, 1, 1, 1, 1]:
                    send_note_on(notas['RE'])
                elif dedos == [0, 1, 1, 1, 0]:
                    send_note_on(notas['MI'])
                elif dedos == [0, 1, 1, 0, 0]:
                    send_note_on(notas['FA'])
                elif dedos == [0, 1, 0, 0, 0]:
                    send_note_on(notas['SOL'])
                elif dedos == [1, 0, 0, 0, 0]:
                    send_note_on(notas['LA'])
                elif dedos == [1, 0, 0, 0, 1]:
                    send_note_on(notas['SI'])
                elif dedos == [0, 1, 0, 0, 1]: 
                    if not batida_ativa:
                        midiout.send_message([0x90, 36, 127]) 
                        batida_ativa = True
                elif sum(dedos) == 0:
                    send_note_off()
                    if batida_ativa:
                        midiout.send_message([0x80, 36, 0])
                        batida_ativa = False
                    if efeito_autotune_ativo:
                        send_cc(1, 0) 
                        efeito_autotune_ativo = False
                else:
                    send_note_off()
                    batida_ativa = False

                if altura < 0.2:
                    if not efeito_autotune_ativo:
                        send_cc(1, 127) 
                        efeito_autotune_ativo = True
                else:
                    if efeito_autotune_ativo:
                        send_cc(1, 0) 
                        efeito_autotune_ativo = False

        else:
            send_note_off()
            batida_ativa = False

        cv2.imshow("Controlador MIDI por Gestos", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    send_note_off()
    midiout.close_port()
    cap.release()
    cv2.destroyAllWindows()
