import random

class Jogo:
    def __init__(self):
       self.valor = None
       self.aleatorio = None

    def recebernumero(self):
        while True:
            try:
                self.valor = int(input('Digite o seu numero: '))
                break
            except ValueError:
                print('Entrada inválida. Por favor digite um número inteiro.\n')

    def comparar_numero(self):
        if self.valor > self.aleatorio:
            print('Número muito grande\n')
        elif self.valor < self.aleatorio:
            print('Número muito pequeno\n')
        elif self.valor == self.aleatorio:
            print("Parabéns você acertou!, deseja jogar novamente?")
            return True
        return False

    def logica(self):
        print('_____________________________________\n'
              '....Adivinhe o número!....\n')
        print('Escolha um número de 0 a 30!!\n')
        while True:
            opcao = input("\n Digite y para jogar ou digite n para sair: ")
            if opcao.lower() == 'n':
                print('saindo do jogo...')
                break
            elif opcao.lower() == 'y':
                self.aleatorio = random.randint(0, 30)
                print('\n'
                      '.........Adivinhe o número!.........\n')
                for x in range(5,0,-1):
                    print(f' Tentativa: {x}')
                    self.recebernumero()
                    self.comparar_numero()
                    if self.valor == self.aleatorio:
                        break
                    if x == 1:
                        print(f"Errado! o número era: {self.aleatorio}, deseja tentar novamente?")
            else:
                print('Entrada inválida, tente novamente...')
jogo = Jogo()
jogo.logica()