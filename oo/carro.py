"""
vc deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) motor 
2) direcao

O motor tera a responsabilidade de controlar a velocidade. ele oferece os seguintes atributosL:

1) atributo de dado velocidade
2) Metodo acelerar, que devera incrementar a velocidade em uma unidade.
3) Metodo frear que devera decrementar a velocidade em duas unidades

A direcao tera a responsabilidade de controlar a direcao. Ela oferece os seguintes atributos:

1) Valor de direcao com valores possiveis norte, sul, leste e oeste.
2) Metodo girar_a_direita
3) Metodo girar_a_esquerda

  N
S   L
  O
    Exemplo: 
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    
    >>> #Testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> direcao.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
class Carro: 
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
        
    def frear(self):
        self.motor.frear()
        
    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()
      
class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
       
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]

