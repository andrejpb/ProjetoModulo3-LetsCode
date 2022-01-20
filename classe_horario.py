class Horario:

    def __init__(self, h, m, s):

        self.hora = h
        self.minuto = m
        self.segundo = s

    def __repr__(self):

        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

    def __add__(self, other):

        s_hora = self.hora + other.hora
        s_minuto = self.minuto + other.minuto
        s_segundo = self.segundo + other.segundo

        while s_segundo >= 60:
            s_minuto += 1
            s_segundo -= 60

        while s_minuto >= 60:
            s_hora += 1
            s_minuto -= 60

        while s_hora >= 24:
            s_hora -= 24

        return Horario(s_hora, s_minuto, s_segundo)

    def __gt__(self, other):
        if self.hora > other.hora:
            return True

        elif self.hora == other.hora and self.minuto > other.minuto:
            return True

        elif self.hora == other.hora and self.minuto == other.minuto and self.segundo > other.segundo:
            return True

        else:
            return False

    def __sub__(self, other):

        s_hora = self.hora * 3600
        s_minuto = self.minuto * 60
        s_segundo = self.segundo
        s_tempo = (s_hora + s_minuto + s_segundo)

        o_hora = other.hora * 3600
        o_minuto = other.minuto * 60
        o_segundo = other.segundo
        o_tempo = (o_hora + o_minuto + o_segundo)

        so_tempo = (s_tempo - o_tempo)
        so_hora = 0
        so_minuto = 0
        so_segundo = 0

        while so_tempo >= 3600:
            so_hora += 1
            so_tempo -= 3600

        while so_tempo >= 60:
            so_minuto += 1
            so_tempo -= 60

        so_segundo = so_tempo

        return Horario(so_hora, so_minuto, so_segundo)

