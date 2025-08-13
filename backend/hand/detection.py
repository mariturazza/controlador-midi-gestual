def detectar_dedos(mao, hand_label):
    dedos = []
    for i, tip_id in enumerate([4, 8, 12, 16, 20]):
        if tip_id == 4: 
            if (hand_label == 'Right' and mao.landmark[tip_id].x < mao.landmark[tip_id - 2].x) or \
               (hand_label == 'Left' and mao.landmark[tip_id].x > mao.landmark[tip_id - 2].x):
                dedos.append(1)
            else:
                dedos.append(0)
        else:
            dedos.append(1 if mao.landmark[tip_id].y < mao.landmark[tip_id - 2].y else 0)
    return dedos

def altura_mao(mao):
    return mao.landmark[0].y
