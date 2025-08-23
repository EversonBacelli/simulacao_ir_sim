
class Estatistica:
    resultado = []
    def __init__(self, origem, objetivo, s1TempoProcess, s1RAM, s1RAMPico, s2TempoProcess, s2RAM, s2RAMPico, numeroNos, ciclo, totalRAM):
        self.origem = origem
        self.objetivo = objetivo
        self.s1TempoProcess = s1TempoProcess
        self.s1RAM = s1RAM
        self.s1RAMPico = s1RAMPico
        self.s2TempoProcess = s2TempoProcess
        self.s2RAM = s2RAM
        self.s2RAMPico = s2RAMPico
        self.numeroNos = numeroNos
        self.tempoCiclo = ciclo
        self.totalRAM = totalRAM
        Estatistica.resultado.append(self)
    
