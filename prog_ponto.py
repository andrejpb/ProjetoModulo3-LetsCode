import time

sair = True

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

class SistemaDePonto: #Sistema de Ponto
    funcionarios = dict()

    def __init__(self, name=None, e1=None, s1=None, e2=None, s2=None):
        self.nome = name
        self.entrada1 = e1
        self.saida1 = s1
        self.entrada2 = e2
        self.saida2 = s2

    def cadastro(self):
        self.nome = input("Digite o nome do funcionário: ")
        self.funcionarios[self.nome] = {"Entrada1": self.entrada1,
                                                    "Saida1": self.saida1,
                                                    "Entrada2": self.entrada2,
                                                    "Saida2": self.saida2,
                                                    }
        print()
        print("Cadastro realizado com sucesso")
        time.sleep(2)
        print("\n" * 130)

    def printa_ponto(self):
        print()
        for i, j in self.funcionarios.items():
           print(i)
           for k, l in j.items():
               print(f"{k} ----> {l[0]}:{l[1]}:{l[2]}")
        print()
        print(f"Hoje você trabalhou {self.qtd_trabalhada} horas")
        print(f"Você descansou no intervalo {self.tempo_de_intervalo} horas")
        if self.qtd_trabalhada > Horario(10,00,00):
            print("Você excedeu o horario maximo permitido. Consulte seu gestor")
        print("\nRegistro de ponto impresso com sucesso")
        time.sleep(2)
        print("\n" * 130)

    def primeira_entrada(self):
        if self.nome != None:
            print()
            self.entrada1 = input("Digite a primeira Entrada: hh:mm:ss").split(":")
            self.funcionarios[self.nome]["Entrada1"] = self.entrada1
            self.p_e = Horario(int(self.entrada1[0]), int(self.entrada1[1]), int(self.entrada1[2]))
            print()
            print(f"Entrada realizada com sucesso!\nBom dia, {self.nome}\nTenha um ótimo dia de trabalho!")
            time.sleep(2)
            return self.p_e
        else:
            print("Você precisa cadastrar um funcionário primeiro")
            time.sleep(2)
            print("\n" * 130)
            pass

    def primeira_saida(self):
        if self.entrada1 != None and self.nome != None:
            print()
            self.saida1 = input("Digite a primeira Saída: hh:mm:ss").split(":")
            self.funcionarios[self.nome]["Saida1"] = self.saida1
            self.p_s = Horario(int(self.saida1[0]), int(self.saida1[1]), int(self.saida1[2]))
            print("Saída para o almoço realizada com sucesso! Bom apetite!")
            time.sleep(2)
            return self.p_s
        else:
            print("Seu ponto de entrada não consta nos registros.")
            time.sleep(2)
            print("\n" * 130)
            pass

    def segunda_entrada(self):
        if self.saida1 != None and self.entrada1 != None:
            print()
            self.entrada2 = input("Digite a segunda Entrada: hh:mm:ss").split(":")
            self.s_e = Horario(int(self.entrada2[0]), int(self.entrada2[1]), int(self.entrada2[2]))

            self.diferenca = (int(self.entrada2[0]) - int(self.saida1[0]))

            if self.diferenca > 0:
                self.funcionarios[self.nome]["Entrada2"] = self.entrada2
                print("Segunda entrada realizada com sucesso")
                time.sleep(2)
                return self.s_e
            else:
                print("Seu tempo de descanso deve ser no mínimo de 1h. Tente mais tarde")
                time.sleep(2)
                print("\n" * 130)
        else:
            print("Seu ponto de saída não consta nos registros.")
            time.sleep(2)
            print("\n" * 130)
            pass

    def fim_do_expediente(self):
        if self.entrada2 != None and self.entrada1 != None:
            print()
            self.saida2 = input("Digite a hora do término do expediente: hh:mm:ss").split(":")
            self.funcionarios[self.nome]["Saida2"] = self.saida2
            self.f_e = Horario(int(self.saida2[0]), int(self.saida2[1]), int(self.saida2[2]))

            print(f"Saída realizada com sucesso! Tenha um ótimo descanso, {self.nome}")
            print()

            time.sleep(2)

            return self.f_e

        else:
            print("Você não bateu o ponto de entrada do almoço")
            time.sleep(2)
            print("\n" * 130)
            pass

    def calcula_hora(self):
        self.tempo_de_intervalo = (self.s_e - self.p_s)
        self.qtd_trabalhada = ((self.f_e - self.p_e) - self.tempo_de_intervalo)

    def tela_inicial(self):
        print(23 * "-=")
        print("                    Sistema de Ponto                    ")
        print(23 * "-=")

        print(f"Escolha a opção:\n\t(a) Cadastro\n\t(b) Inicio do Dia\n\t(c) Saída pro Almoço\n\t(d) Volta do Almoço\n\t(e) Fim do Expediente\n\t(f) Visualizar Ponto\n\t(s) Sair")
        opcao = input("Opção Escolhida: ").lower()

        if opcao == "a":
            a.cadastro()

        if opcao == "b":
            a.primeira_entrada()

        if opcao == "c":
            a.primeira_saida()

        if opcao == "d":
            a.segunda_entrada()

        if opcao == "e":
            a.fim_do_expediente()

        if opcao == "f":
            a.calcula_hora()
            a.printa_ponto()

        if opcao == "s":
            return False

        if opcao == "x":
            a.calcula_hora()


a = SistemaDePonto()

while True:
    sair = a.tela_inicial()
    if sair == False:
        print("Obrigado por usar nosso Sistema de Ponto")
        print("Bye!!!!")
        break

