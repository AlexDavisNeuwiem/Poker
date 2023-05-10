from PokerClasses import Baralho, Poker

p = Poker()

inicio = False

while True:
    
    a = str(input('\n(1) Iniciar Partida  (2) Mostrar Cartas (3) Pré-Flop\n(4) Flop             (5) Turn           (6) River\n(7) Terminar Partida (R) Resposta: '))
    while not (a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7'):
        print('\n>> Valor Inválido!')
        a = str(input('\n(1) Iniciar Partida  (2) Mostrar Cartas (3) Pré-Flop\n(4) Flop             (5) Turn           (6) River\n(7) Terminar Partida (R) Resposta: '))
    
    if (a == '1'):
        if(inicio == False):
            p.deck.embaralhar()
            print('\n>> Deck Embaralhado!')
                
            p.distribuir()
            print('>> Deck Distribuído!')
            
            inicio = True
            
        else:
            print('\n>> Partida já iniciada!')

    elif (a == '2'):
        p.mostrar()
    
    elif (a == '3'):
        p.partida('PRÉ-FLOP')
    
    elif (a == '4'):
        p.partida('FLOP')
        
    elif (a == '5'):
        p.partida('TURN')
        
    elif (a == '6'):
        p.partida('RIVER')

    else:
        break

print('\n>> Programa Encerrado!')