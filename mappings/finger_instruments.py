class FingerInstrumentMap:
    def __init__(self):
        self.mapeamento_maos = {}         # 'Right' e 'Left'
        self.instrumentos_canais = {}     # 'guitarra': 1, etc.

    def carregar_mapeamento_maos(self, dados_maos: dict):
        self.mapeamento_maos = dados_maos

    def carregar_canais(self, canais: dict):
        self.instrumentos_canais = canais

    def get_info_dedo(self, mao: str, dedo_index: int):
        """
        Retorna (nota/som, canal MIDI) para uma mão e dedo específicos.
        """
        mao_data = self.mapeamento_maos.get(mao)
        if not mao_data:
            return None, None

        escala = mao_data.get("escala", [])
        instrumento = mao_data.get("instrumento")
        canal = self.instrumentos_canais.get(instrumento)

        if dedo_index < len(escala):
            return escala[dedo_index], canal

        return None, canal
