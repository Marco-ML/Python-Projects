import turtle as t
import random
import math
import time

db = { 'Nível 1' : {'Fruta': ['banana', 'maça', 'melancia', 'melao', 'limao'],
         'Objeto' : ['tesoura', 'celular', 'lapiseira', 'caneta', 'vassoura'],
         'País' : ['brasil', 'canada', 'argentina', 'china', 'india']                   
                   },
     
        'Nível 2' : {'Fruta' : ['cupuaçu', 'pitaia', 'carambola', 'tamarindo', 'kiwi'],
            'Objeto' : ['grampeador', 'alicate', 'xicara', 'tijolo', 'telefone'],
            'País' : ['peru', 'angola', 'somalia', 'frança', 'iraque']        
                    },
     
         'Nível 3' : {'Fruta ' : ['mangostim', 'kiwano', 'tamarilho', 'longan', 'salak'],
             'Objeto ' : ['bisturi', 'ampulheta', 'candelabro', 'anzol', 'cemaforo'],
             'País' : ['nauru', 'tuvalu', 'liechtenstein', 'djibouti', 'moldavia']        
                     }
     }

vitorias = 0

def retangulo(base: float, altura: float, angulo: float, color: str):
    '''
    Função que recebe o comprimento da base e da altura em pixels,
    o ângulo de inclinação da figura e a cor.
    
    Atributos:
        base: tamanho da base do retângulo(float).
        altura: tamanho da altura do retângulo(float).
        angulo: ângulo de rotação do retângulo(float).
        color: cor do retângulo(str).
    '''
    t.pencolor(color)
    t.left(angulo)
    t.fillcolor(color) #Seleciona a cor de preenchimento
    t.begin_fill() #Inicia o preenchimento
    for i in range(1, 5):
        if i%2 == 0:
            t.forward(altura)
        else:
            t.forward(base)
        t.left(90)
    t.end_fill() #Termina o preenchimento
    
def posicao(deslocamento: float, angulo: float):
    '''
    Função recebe a posição inicial e o ângulo de inclinação e movimenta
    o ponteiro até a posição desejada.
    
    Atributos:
        deslocamento: deslocamento do ponteiro(float).
        angulo: ângulo de rotação da movimentação(float).
    '''
    t.setheading(0) #Coloca o ponteiro na angulação e posição padrão.
    t.up()
    t.left(angulo)
    t.forward(deslocamento)
    t.down()
    t.setheading(0) #Coloca o ponteiro na angulação e posição padrão.

def disco(raio_maior: float, raio_menor: float, color: str, cor_de_fundo: str):
    '''
    Função que recebe o raio maior e o raio menor de duas circunferências,
    a cor e desenha um disco.
    
    Atributo:
        raio_maior: raio da circunferência maior(float).
        raio_menor: raio da circunferência menos(float).
        color: cor da circunferência maior(str).
        cor_de_fundo: cor da circunferência menor(str).
    '''
    t.pencolor(color)
    t.fillcolor(color) #Seleciona a cor de preenchimento
    t.begin_fill() #Inicia o preenchimento
    t.circle(raio_maior)
    t.end_fill()
    posicao(raio_maior/2, 90)
    t.fillcolor(cor_de_fundo) #Seleciona a cor de preenchimento
    t.begin_fill() #Inicia o preenchimento
    t.circle(raio_menor)
    t.end_fill()
    
def circulo(raio: float, color: str):
    '''
    Função que recebe o raio e a cor e desenha um circunferência.
    
    Atributo:
        raio: raio da circunferência(float).
        color: cor da circunferência(str).
    '''
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()
    
def traco(deslocamento: float, angulo: float, color: str):
    '''
    Função que desenha um traço.
    
    Atributos:
        deslocamento: deslocamento percorrido pelo traço(float).
        angulo: ângulo de rotação do traço(float).
        color: cor do traço(str).
    '''
    t.color(color)
    t.left(angulo)
    t.forward(deslocamento)
    t.setheading(0)
    
def desenhar_x(tamanho, angulo, color):
    '''
    Função que desenha um x.
    
    Atributos:
        tamanho: tamanho dos traços(float).
        angulo: ângulo de rotação dos traços(float).
        color: cor dos traços(str).
    '''
    traco(tamanho, angulo, color)
    y = tamanho * math.sin(angulo)
    posicao(y, 90)
    posicao(tamanho, -180)
    posicao(y, -90)
    traco(tamanho, -angulo, color)
    

def etapa_1():
    '''
    Função que desenha a cabeça do personagem.
    '''
    posicao(4, 90)
    circulo(15, 'green')
    
def etapa_2():
    '''
    Função que desenha o tronco do personagem.
    '''
    posicao(4, -90)
    posicao(-5, 0)
    retangulo(10, 4, 0, 'green')
    posicao(35, -90)
    retangulo(10, 28, 0, 'green')

def etapa_3():
    '''
    Função que desenha o braço esquerdo do personagem.
    '''
    posicao(20, 90)
    retangulo(5, 20, 90, 'green')
    
def etapa_4():
    '''
    Função que desenha o braço direito do personagem.
    '''
    posicao(30, 0)
    retangulo(5, 20, 90, 'green')
    
def etapa_5():
    '''
    Função que desenha a perna direita do personagem.
    '''
    posicao(14, -180)
    posicao(35, -90)
    retangulo(5,20,30,'green')
    
def game_over(cor_de_fundo: str):
    '''
    Função que desenha a perna esquerda do personagem e realiza a animação de game over.
    
    Atributos:
        cor_de_fundo: cor de fundo da janela(str).
    '''
    cor_forca = '#7d5514'
    cor_corda = '#de9e35'
    posicao(27, -180)
    retangulo(5, 20, -30, 'green')
    posicao(18, 0)
    posicao(42, 90)
    posicao(2, -180)
    circulo(20, cor_de_fundo)
    posicao(5, 90)
    disco(16, 8, cor_corda, cor_de_fundo)
    circulo(15, 'green')
    posicao(18, -90)
    posicao(4, 0)
    retangulo(10, 8, 90, 'green')
    posicao(2, -90)
    posicao(21, 0) 
    retangulo(5, 20, 90, cor_de_fundo)
    posicao(22, -180)
    posicao(7, 90) #
    retangulo(5,20,220, 'green') 
    posicao(7, -90) 
    posicao(9,-180)
    retangulo(5, 20, 90, cor_de_fundo)
    posicao(6, 0)
    retangulo(5,20,130, 'green') 
    posicao(32, 90)
    posicao(9, -180)
    desenhar_x(10, 30, 'black')
    posicao(6, 0)
    desenhar_x(10, 30, 'black')
    posicao(70, 90)
    t.color('red')
    t.write("GAME OVER!", font=("Verdana", 
                                    30, "normal"),
           align = 'center') 
    
def win(cor_de_fundo: str):
    '''
    Função que realiza a animação de vitória.
    
    Atributos:
        cor_de_fundo: cor de fundo da janela(str).
    '''
    t.up()
    t.sety(150)
    t.color('green')
    t.write("VOCÊ VENCEU!", font=("Verdana", 
                                    30, "normal"),
           align = 'center')
    t.down()
    
def nivel():
    '''
    Função que desenha o nível atual do usuário no jogo.
    '''
    posicao(150, 90)
    posicao(100, -180)
    if vitorias == 0:
        t.color('green')
        t.write("EASY", font=("Verdana", 
                                    30, "normal"),
           align = 'right')
    elif vitorias == 1:
        t.color('blue')
        t.write("MEDIUM", font=("Verdana", 
                                    30, "normal"),
           align = 'right')
    else:
        t.color('red')
        t.write("HARD", font=("Verdana", 
                                    30, "normal"),
        align = 'right')
    t.up()
    t.setx(0)
    t.sety(0)
    t.down()

def entrada() -> str:
    '''
    Função responsável por receber a entrada da letra pelo usuário e retornar a letra.
    
    Retorna:
        letra: letra digitada pelo usuário(str).
    '''
    letra = str(input('Digite uma letra: ')).strip().lower()
    return letra

def checagem_letra() -> str:
    '''
    Função que checa se a entrada do usuário é uma letra e caso realmente seja uma letra, então retorna a letra.
    '''
    letra = entrada()
    while len(letra) != 1:
        letra = entrada()
    return letra

def selecionar_tema_palavra() -> tuple:
    '''
    Função que escolhe de forma aleatória dado o nível as palavras e os temas do banco de dados.
    
    Retorna:
        (tema, palavra): tupla contendo o tema escolhido aleatóriamente e a palavra escolhida aleatóriamente.
    '''
    if vitorias == 0:
        db_aux = db['Nível 1']
    elif vitorias == 1:
        db_aux = db['Nível 2']
    else:
        db_aux = db['Nível 3']
    tema = random.choice(list(db_aux.keys()))
    palavra = random.choice(list(db_aux[tema]))
    return (tema, palavra)

def pontuacao(palavra: str, entrada: str, ponto: int) -> int:
    '''
    Função responsável por reduzir a pontuação, tecebe a palavra, a letra de entrada e a pontuação atual e retorna a nova pontuação.
    
    Atributos:
        palavra: palavra escolhida aleatóriamente(str).
        entrada: letra digitada pelo usuário(str).
        ponto: pontuação atual do usuário(int).
        
    Retorna:
        ponto: pontuação atualizada do usuário(int).
    '''
    if entrada not in palavra:
        ponto -= 1
    return ponto

def front_init(cor_de_fundo = '#2c2d33'):
    '''
    Função responsável por iniciar a parte gráfica do jogo e instanciar a função principal.
    '''
    t.hideturtle()
    cor_forca = '#7d5514'
    cor_corda = '#de9e35'
    t.speed('fastest')
    t.bgcolor(cor_de_fundo)
    t.title("Jogo da forca")
    nivel()
    posicao(80, 90) #Sobe
    posicao(20, 0) #Vai para direita
    retangulo(60, 10, 45, cor_forca)
    posicao(20, -180) #Vai para esquerda
    posicao(40, 90)
    retangulo(100, 20, 0, cor_forca)
    posicao(100, -90)
    retangulo(20,130, 0, cor_forca)
    posicao(100, 90)
    posicao(20, -180)
    retangulo(20, 20, 0, cor_forca)
    posicao(100,0)
    retangulo(30, 10, -90, cor_corda)
    posicao(50, -90)
    posicao(5, 0)
    disco(16, 8, cor_corda, cor_de_fundo)
    main(cor_de_fundo)
    t.mainloop()
    
def main(cor_de_fundo: str):
    '''
    Função principal que é responsável por coordenar a parte lógica do jogo.
    '''
    global vitorias
    ponto = 6
    tema, palavra = selecionar_tema_palavra()
    print('Tema: ', tema)
    lista_apresentacao = ['_']*len(palavra)
    while True:
        ponto2 = ponto
        apresentacao = ' '.join(lista_apresentacao)
        apresentacao_bool = ''.join(lista_apresentacao)
        print(apresentacao)
        if (ponto > 0) and (apresentacao_bool != palavra):
            entrada = checagem_letra()
            if entrada in apresentacao:
                print('Letra já selecionada.')
            else:
                ponto = pontuacao(palavra, entrada, ponto)
                index = []
                for i in range(0, len(palavra)):
                    if entrada == palavra[i]:
                        index.append(i)
                for i in index:
                    lista_apresentacao[i] = entrada
                if (ponto == 5) and (ponto2 > ponto):
                    etapa_1()
                elif (ponto == 4) and (ponto2 > ponto):
                    etapa_2()
                elif (ponto == 3) and (ponto2 > ponto):
                    etapa_3()
                elif (ponto == 2) and (ponto2 > ponto):
                    etapa_4()
                elif (ponto == 1) and (ponto2 > ponto):
                    etapa_5()
                elif ponto == 0:
                    game_over(cor_de_fundo)
                    resposta = input('Deseja tentar novamente(S/N)? ').upper()
                    if resposta == 'S':
                        vitorias = 0
                        t.reset()
                        front_init('#2c2d33')
                    else:
                        t.bye()
        else:
            vitorias += 1
            win(cor_de_fundo)
            time.sleep(4)
            if vitorias < 3:
                t.reset()
                front_init('#2c2d33')
            else:
                resposta = input('Deseja recomeçar(S/N)? ').upper()
                if resposta == 'S':
                    vitorias = 0
                    t.reset()
                    front_init('#2c2d33')
                else:
                    t.bye()

front_init()