elif hand_label == 'Left':
                        canal_esquerdo = 1
                        if dedos == [1, 1, 1, 1, 1]:
                            if not loop_flags['left']:
                                start_loop('left', 'bass', velocity, canal_esquerdo)
                        elif dedos == [0, 1, 1, 1, 1]:
                            send_note_on(notas_guitarra['5-3'], hand='left', velocity=velocity, canal=canal_esquerdo)
                        else:
                            send_note_off(hand='left', canal=canal_esquerdo)
                            stop_loop('left')