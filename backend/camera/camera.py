import cv2
from hand.mediapipe import hands, mp_drawing, mp_hands

def process_frame(frame):
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    return results, bgr

def draw_hand(image, hand_landmarks):
    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
