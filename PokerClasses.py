import random

class Baralho:
    def __init__(self):
        self.baralho = []
        simb = ['♠', '♣', '♥', '♦']
        valor = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        for a in simb:
            for b in valor:
                self.baralho.append(b+a)
    
    def embaralhar(self):
        random.shuffle(self.baralho)

class Poker:
    
    def __init__(self):
        self.total = int(input('\nDigite a quantidade de jogadores: '))
        while not (2 <= self.total <= 10):
            print('\n>> Valor Inválido!')
            self.total = int(input('\nDigite a quantidade de jogadores: '))
        self.deck = Baralho()
        self.cartas = []
        self.mesa = []
        self.montante = 0
   
        for i in range(self.total):
            self.cartas.append(i)
            self.cartas[i] = []
       
    def distribuir(self):
        c = g = 0
        d = 52 - (52 % self.total)
        
        while (c < d):
            for index, value in enumerate(self.cartas):
                if ( len(value) < 2 ): 
                    self.cartas[index].append(self.deck.baralho[c])
                    self.deck.baralho.pop(c)
                c += 1
        
        while (len(self.mesa) < 5):
            self.mesa.append(self.deck.baralho[g])
            self.deck.baralho.pop(g)
            g += 1
        
    def partida(self, part):
        if( len(self.mesa) > 0 ):
            
            if(part == 'RIVER'):
                
                print('\n{} {} {} {} {}'.format(self.mesa[0], self.mesa[1], self.mesa[2], self.mesa[3], self.mesa[4]))
                print('\n>> Montante: R${:.2f}'.format(self.montante))

            else:
            
                if(part == 'PRÉ-FLOP'):
                    pass
                    
                elif(part == 'FLOP'):
                    print('\n{} {} {}'.format(self.mesa[0], self.mesa[1], self.mesa[2]))
                    
                elif(part == 'TURN'):
                    print('\n{} {} {} {}'.format(self.mesa[0], self.mesa[1], self.mesa[2], self.mesa[3]))
                    
                else:
                    print('\n>> Partida Não Especificada!')
                    
                for x in range(self.total):
                    print('\n>> Montante: R${:.2f}'.format(self.montante))
                    jogada = str(input('\nAção do {}º jogador: '.format(x+1))).upper()
                        
                    while not (jogada == 'APOSTAR' or jogada == 'SAIR'):
                        print('\n>> Digite apenas "Apostar" ou "Sair"!')
                        jogada = str(input('Ação do {}º jogador: '.format(x+1))).upper()
                        
                    if(jogada == 'APOSTAR'):
                        aposta = float(input('\nValor da Aposta: '))
                            
                        while (aposta <= 0):
                            print('\n>> Valor Inválido!')
                            aposta = float(input('\nValor da Aposta: '))
                                
                        self.montante = self.montante + aposta
                        
                    else:
                        if(self.total == 2):
                            print('\n>> Partida Encerrada!')
                            break
                        else:
                            self.total = self.total - 1
                            self.cartas.pop(x)
            
        else:
            print('\n>> Cartas Não Distribuídas!')
    
    def mostrar(self):
            
        for pos, val in enumerate(self.cartas):
            print('\nCartas do {}º jogador: {}'.format((pos + 1), val)) 
        
        print('\nCartas Restantes:', len(self.deck.baralho))